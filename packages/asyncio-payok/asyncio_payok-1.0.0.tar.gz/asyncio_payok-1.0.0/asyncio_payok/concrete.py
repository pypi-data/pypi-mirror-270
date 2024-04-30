from abc import ABC

from base import MakeRequestCommand, FormatCommand, AbstractHandler, Formatter, ResponseFacade, Operation, \
	OperationFactory
from aiohttp import ClientSession
from typing import Dict
from const import Types, Method, ApiError, Currencies
from pydantic import BaseModel, ValidationError
from functools import wraps
from typing import Union, List, Optional

class ConcreteMakeRequestCommand(MakeRequestCommand):
	const_url = 'https://payok.io/'

	def __init__(self, next_command: FormatCommand):
		super().__init__(next_command)

	async def update(self, type: Types, method: Method, **kwargs) -> dict:
		url = f'{self.const_url}{type.value}'
		async with ClientSession() as session:
			async with session.request(method.value, url, **kwargs) as response:
				response = await response.json(content_type="text/plain")
				return response

	async def handle_update(self, type: Types, method: Method, **kwargs):
		try:
			data = kwargs['data']
		except KeyError:
			raise KeyError('data is required')
		result = await self.update(type, method, data=data)
		try:
			final = await self.next_command.handle_update(result)
			return final
		except NotImplementedError:
			return await self.next_command.update(result)


class ConcreteRequestFormatter(Formatter):
	@staticmethod
	async def format_response(response: dict):
		try:
			assert 'status' in response.keys() and response['status'] == 'error'
		except AssertionError:
			return response
		else:
			raise ApiError(code=response['error_code'],
			               text=response['text'] if response.get('text') else response['error_text'])


class ConcreateRequestHandler(AbstractHandler):
	def __init__(self, successor: ConcreteMakeRequestCommand = ConcreteMakeRequestCommand(
		next_command=FormatCommand(
			facade=ResponseFacade(
				formatter=ConcreteRequestFormatter())))):
		super().__init__(successor)

	async def handle_update(self, type: Types, method: Method, data: dict):
		return await self.successor.handle_update(type, method, data=data)


class ConcreteOperationFactory(OperationFactory):
	def __init__(self, operations: Dict[str, Operation] = None):
		super().__init__(operations)


class ConcreteOperation(Operation, ABC):
	def __init__(self, handler: Optional[ConcreateRequestHandler] = None):
		self.__handler = handler if handler else None

	async def _make_request(self, type: Types, method: Method, data: dict):
		if not self.__handler:
			raise NotImplementedError
		res = await self.__handler.handle_update(type, method, data=data)
		return res


class ValidationDecorator:

	def __init__(self, model: BaseModel):
		self._model = model

	async def __from_dict(self, data: dict) -> Union[BaseModel, List[BaseModel]]:
		try:
			values = [self._model.validate(x) for x in data.values() if isinstance(x, dict)]
			if not values:
				return self._model.validate(data)
			return values
		except KeyError or ValueError:
			return self._model.validate(data)

	async def validate(self, data: dict):
		try:
			return await self.__from_dict(data)
		except ValidationError as e:
			return data

	def __call__(self, func):
		@wraps(func)
		async def wrapper(*args, **kwargs):
			result = await func(*args, **kwargs)
			return await self.validate(result)

		return wrapper
