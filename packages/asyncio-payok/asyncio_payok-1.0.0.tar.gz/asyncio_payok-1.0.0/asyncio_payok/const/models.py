from pydantic import BaseModel
from typing import Union


class Transaction(BaseModel):
	"""Payok API transaction model"""

	transaction: int = None
	email: str = None
	amount: float = None
	currency: str = None
	currency_amount: float = None
	comission_percent: float = None
	comission_fixed: float = None
	amount_profit: float = None
	method: Union[str, None] = None
	payment_id: Union[int, str] = None
	description: str = None
	date: str = None
	pay_date: str = None
	transaction_status: int = None
	custom_fields: str = None
	webhook_status: int = None
	webhook_amount: int = None


class Balance(BaseModel):
	"""Payok API balance model"""

	balance: float = None
	ref_balance: float = None


class Payout(BaseModel):
	"""Payok API payout model"""

	payout_id: int = None
	method: Union[str, None] = None
	amount: float = None
	comission_percent: float = None
	comission_fixed: float = None
	amount_profit: float = None
	date_create: str = None
	date_pay: str = None
	status: str = None


class DataPayout(BaseModel):
	"""Payok API payout model"""
	payout_id: int = None
	method: str = None
	amount: float = None
	comission_percent: float = None
	comission_fixed: float = None
	amount_profit: float = None
	date: str = None
	payout_status_code: int = None
	payout_status_text: str = None


class CreatedPayout(BaseModel):
	"""Payok API created payout model"""

	status: str = None
	remain_balance: float = None
	data: DataPayout = None
