from operations import BalanceOperation, PayoutOperation, TransactionOperation, CreatePayoutOperation, \
	CreatePayUrlOperation
from concrete import ConcreteOperationFactory, ConcreateRequestHandler, ConcreteOperation
from const import Types, Method, Balance, Transaction, Payout, CreatedPayout, Currencies
from typing import Optional, Union, List
import asyncio
from any_utils import Timer
FACTORY_OPERATIONS = {
	'balance': BalanceOperation(ConcreateRequestHandler()),
	'payout': PayoutOperation(ConcreateRequestHandler()),
	'transaction': TransactionOperation(ConcreateRequestHandler()),
	'create_payout': CreatePayoutOperation(ConcreateRequestHandler()),
	'create_pay_url': CreatePayUrlOperation()
}


class PayOk:

	def __init__(self, api_id: int, api_key: str, secret_key: Optional[str] = None, shop: Optional[int] = None):
		self.__api_id = api_id
		self.__api_key = api_key
		self.__secret_key = secret_key
		self.__shop = shop
		self.__factory = ConcreteOperationFactory(FACTORY_OPERATIONS)

	async def __create(self, type: str) -> ConcreteOperation:
		return await self.__factory.create(type)

	async def get_balance(self) -> Balance:
		"""
		Async function to get balance.

		:return: Balance
		"""
		instance = await self.__create('balance')
		return await instance.execute(self.__api_id, self.__api_key)

	async def get_transaction(self, payment_id: Optional[int] = None,
	                          offset: Optional[int] = None) -> Union[Transaction, List[Transaction]]:
		"""
		Async function to get a transaction.

		:param payment_id: Optional[int]
		:param offset: Optional[int]
		:return: Union[Transaction, List[Transaction]]
		"""
		instance = await self.__create('transaction')
		return await instance.execute(self.__api_id, self.__api_key, self.__shop, payment_id, offset)

	async def get_payout(self, payout: Optional[int] = None, offset: Optional[int] = None) -> Union[
		Payout, List[Payout]]:
		"""
		Async function to get a payout.

		:param payout: Optional[int]
		:param offset: Optional[int]
		:return: Union[Payout, List[Payout]]
		"""
		instance = await self.__create('payout')
		return await instance.execute(self.__api_id, self.__api_key, payout, offset)

	async def create_payout(
			self,
			amount: float,
			receiver: str,
			sbp_bank: Optional[str] = None,
			commission_type: str = 'balance', webhook_url: Optional[str] = None,
			method: str = 'card'
	) -> CreatedPayout:
		"""
		Asynchronously creates a payout with the given amount, receiver, and optional parameters.
		:param amount:
		:param receiver:
		:param sbp_bank:
		:param commission_type:
		:param webhook_url:
		:param method:
		:return: An instance of CreatedPayout representing the created payout.
		"""
		instance = await self.__create('create_payout')
		return await instance.execute(self.__api_id, self.__api_key, amount, receiver, sbp_bank, commission_type,
		                              webhook_url, method)

	async def create_pay(
			self,
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
		"""
		Asynchronously creates a payment with the given amount, payment, and optional parameters.
		:param amount:
		:param payment:
		:param currency:
		:param desc:
		:param email:
		:param success_url:
		:param method:
		:param lang:
		:param custom:
		:return: A string representing the payment URL.
		"""
		instance = await self.__create('create_pay_url')
		return await instance.execute(self.__shop, self.__secret_key, amount, payment, currency, desc, email,
		                              success_url, method, lang, custom)


