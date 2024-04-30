from typing import List

import requests
from requests import HTTPError

from ynabtransactionadjuster.models import CategoryGroup, ModifiedTransaction
from ynabtransactionadjuster.models import Transaction
from ynabtransactionadjuster.models import Payee
from ynabtransactionadjuster.models.account import Account
from ynabtransactionadjuster.models.credentials import Credentials

YNAB_BASE_URL = 'https://api.ynab.com/v1'


class Client:
	"""Client for reading from and writing to YNAB

	:param token: YNAB API token
	:param budget: YNAB budget ID
	:param account: YNAB account ID
	"""

	def __init__(self, token: str, budget: str, account: str):
		self._header = {'Authorization': f'Bearer {token}'}
		self._budget = budget
		self._account = account

	@classmethod
	def from_credentials(cls, credentials: Credentials):
		return cls(token=credentials.token, budget=credentials.budget, account=credentials.account)

	def fetch_categories(self) -> List[CategoryGroup]:
		"""Fetches categories from YNAB"""
		r = requests.get(f'{YNAB_BASE_URL}/budgets/{self._budget}/categories', headers=self._header)
		r.raise_for_status()

		data = r.json()['data']['category_groups']
		categories = [CategoryGroup.from_dict(cg) for cg in data if cg['deleted'] is False]
		return categories

	def fetch_payees(self) -> List[Payee]:
		"""Fetches payees from YNAB"""
		r = requests.get(f'{YNAB_BASE_URL}/budgets/{self._budget}/payees', headers=self._header)
		r.raise_for_status()

		data = r.json()['data']['payees']
		payees = [Payee.from_dict(p) for p in data if p['deleted'] is False]
		return payees

	def fetch_accounts(self) -> List[Account]:
		"""Fetches accounts from YNAB"""
		r = requests.get(f'{YNAB_BASE_URL}/budgets/{self._budget}/accounts', headers=self._header)
		r.raise_for_status()

		data = r.json()['data']['accounts']
		accounts = [Account(name=a['name'], id=a['id']) for a in data if a['deleted'] is False]
		return accounts

	def fetch_transactions(self, account_id: str = None) -> List[Transaction]:
		"""Fetches transactions from YNAB

		:param account_id: Optional YNAB account ID to fetch only for specific account
		"""
		account_part_url = f'accounts/{account_id}/' if account_id else ''
		r = requests.get(f'{YNAB_BASE_URL}/budgets/{self._budget}/{account_part_url}transactions', headers=self._header)
		r.raise_for_status()

		data = r.json()['data']['transactions']
		transaction_dicts = [t for t in data if t['deleted'] is False]
		transactions = [Transaction.from_dict(t) for t in transaction_dicts]
		return transactions

	def fetch_transaction(self, transaction_id: str) -> Transaction:
		r = requests.get(f'{YNAB_BASE_URL}/budgets/{self._budget}/transactions/{transaction_id}', headers=self._header)
		r.raise_for_status()
		return Transaction.from_dict(r.json()['data']['transaction'])

	def update_transactions(self, transactions: List[ModifiedTransaction]) -> List[Transaction]:
		"""Updates transactions in YNAB. The updates are done in bulk.

		:param transactions: list of modified transactions to be updated
		:raises HTTPError: if bulk update call is not successful. Error can be related to any item in the passed list
		of transactions
		"""
		update_dict = {'transactions': [r.as_dict() for r in transactions]}
		r = requests.patch(f'{YNAB_BASE_URL}/budgets/{self._budget}/transactions',
						   json=update_dict,
						   headers=self._header)
		try:
			r.raise_for_status()
		except HTTPError as e:
			raise HTTPError(r.text, update_dict)
		r_dict = r.json()['data']
		updated_transactions = [Transaction.from_dict(t) for t in r_dict['transactions'] if t['id'] in [t.transaction.id for t in transactions]]
		return updated_transactions
