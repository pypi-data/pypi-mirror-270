from concrete import ConcreateRequestHandler, ConcreteOperation, ValidationDecorator as validator
from const import Types, Method, Balance, Transaction, Payout, CreatedPayout, Currencies
from typing import Optional, Union, List
from any_utils import Timer
from urllib.parse import urlencode
from hashlib import md5
class BalanceOperation(ConcreteOperation):
	def __init__(self, handler: ConcreateRequestHandler):
		super().__init__(handler=handler)

	@validator(Balance())
	async def execute(self, api_id: int, api_key: str) -> Balance:
		return await self._make_request(Types.BALANCE, Method.POST, data={'API_ID': api_id, 'API_KEY': api_key})


class TransactionOperation(ConcreteOperation):
	def __init__(self, handler: ConcreateRequestHandler):
		super().__init__(handler=handler)

	@validator(Transaction())
	async def execute(self, api_id: int, api_key: str, shop: int, payment_id: Optional[int] = None,
	                  offset: Optional[int] = None) -> Union[Transaction, List[Transaction]]:
		data = {
			'API_ID': api_id,
			'API_KEY': api_key,
			'shop': shop,
		}
		if payment_id:
			data['payment_id'] = payment_id
		if offset:
			data['offset'] = offset
		return await self._make_request(Types.TRANSACTIONS, Method.POST, data=data)


class PayoutOperation(ConcreteOperation):
	def __init__(self, handler: ConcreateRequestHandler):
		super().__init__(handler=handler)

	@validator(Payout())
	async def execute(self, api_id: int, api_key: str, payout: Optional[int] = None, offset: Optional[int] = None) -> Union[Payout, List[Payout]]:
		data = {
			'API_ID': api_id,
			'API_KEY': api_key,
		}
		if payout:
			data['payout'] = payout
		if offset:
			data['offset'] = offset
		return await self._make_request(Types.PAYOUT, Method.POST, data=data)


class CreatePayoutOperation(ConcreteOperation):
	def __init__(self, handler: ConcreateRequestHandler):
		super().__init__(handler=handler)

	@validator(CreatedPayout())
	async def execute(
			self,
			api_id: int,
			api_key: str,
			amount: float,
			receiver: str,
			sbp_bank: Optional[str] = None,
			commission_type: str = 'balance',
			webhook_url: Optional[str] = None,
			method: str = 'card'
	) -> CreatedPayout:

		data = {
			'API_ID': api_id,
			'API_KEY': api_key,
			'amount': amount,
			'receiver': receiver,
			'commission_type': commission_type,
			'method': method
		}
		if sbp_bank:
			data['sbp_bank'] = sbp_bank
		if webhook_url:
			data['webhook_url'] = webhook_url
		return await self._make_request(Types.PAYOUT, Method.POST, data=data)


class CreatePayUrlOperation(ConcreteOperation):
	def __init__(self):
		self.__const_url = 'https://payok.io/'
		super().__init__()

	async def execute(
			self,
			shop: int,
			secret_key: str,
			amount: float,
			payment: Union[int, str],
			currency: Optional[str] = Currencies.RUB.value,
			desc: Optional[str] = 'Description',
			email: Optional[str] = None,
			success_url: Optional[str] = None,
			method: Optional[str] = None,
			lang: Optional[str] = None,
			custom: Optional[str] = None
	) -> str:
		url = self.__const_url + Types.PAY.value + '?'
		data = {
			'amount': amount,
			'payment': payment,
			'shop': shop,
			'currency': currency,
			'desc': desc
		}
		if email:
			data['email'] = email
		if success_url:
			data['success_url'] = success_url
		if method:
			data['method'] = method
		if lang:
			data['lang'] = lang
		if custom:
			data['custom'] = custom

		data['sign'] = await self.__sign([*list(data.values())[:5], secret_key])

		return url + urlencode(data)

	@staticmethod
	async def __sign(params: list) -> str:
		sign = '|'.join(map(str, params)).encode('utf-8')
		return md5(sign).hexdigest()
