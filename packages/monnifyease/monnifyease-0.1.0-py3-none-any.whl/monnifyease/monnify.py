""" Wrapper classes for various Synchronous Monnify API endpoints,
providing simplified access to functionality in Monnify
"""

from monnifyease.apis import (
    customer_reserved_account,
    transactions
)


class Monnify:
    """Monnify acts as a wrapper around various client APIs to
    interact with the Monnify API
    """
    def __init__(self) -> None:
        self.reserve_account = customer_reserved_account.CustomerReservedAccount()
        self.transactions = transactions.Transactions()
