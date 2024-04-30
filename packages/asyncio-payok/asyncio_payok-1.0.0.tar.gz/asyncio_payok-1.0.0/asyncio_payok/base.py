from abc import ABC, abstractmethod
from typing import Dict


class Formatter:
	@staticmethod
	async def format_response(response: dict):
		return response


class ResponseFacade(ABC):
	def __init__(self, formatter: Formatter):
		self.formatter = formatter

	def do_format(self, response: dict):
		return self.formatter.format_response(response)


class Factory(ABC):
	@abstractmethod
	async def create(self, *args, **kwargs):
		pass


class ChainOfResponsibility(ABC):
	@abstractmethod
	async def update(self, *args, **kwargs):
		pass

	@abstractmethod
	async def handle_update(self, *args, **kwargs):
		pass


class AbstractHandler(ABC):

	def __init__(self, successor: ChainOfResponsibility):
		self.successor = successor

	@abstractmethod
	async def handle_update(self, *args, **kwargs):
		pass


class MakeRequestCommand(ChainOfResponsibility, ABC):

	def __init__(self, next_command: ChainOfResponsibility):
		self.next_command = next_command

	@abstractmethod
	async def update(self, *args, **kwargs):
		pass

	@abstractmethod
	async def handle_update(self, *args, **kwargs):
		pass


class FormatCommand(ChainOfResponsibility):

	def __init__(self, facade: ResponseFacade, next_command: ChainOfResponsibility = None):
		self.next_command = next_command
		self._facade = facade

	async def update(self, result):

		return await self._facade.do_format(result)

	async def handle_update(self, *args, **kwargs):
		raise NotImplementedError


class Operation:
	@abstractmethod
	async def execute(self, *args, **kwargs):
		pass


class OperationFactory(Factory):
	def __init__(self, dict_of_operations: Dict[str, Operation] = None):
		self.__type = {} if not dict_of_operations else dict_of_operations

	async def create(self, operation: str):
		try:
			return self.__type[operation]
		except KeyError:
			return None
