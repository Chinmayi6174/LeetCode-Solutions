class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.n = len(balance)

    def _is_valid_account(self, account: int) -> bool:
        # Check if account number is valid
        return 1 <= account <= self.n

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # Validate accounts
        if not self._is_valid_account(account1) or not self._is_valid_account(account2):
            return False
        # Check sufficient funds
        if self.balance[account1 - 1] < money:
            return False
        # Perform transfer
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        # Validate account
        if not self._is_valid_account(account):
            return False
        # Deposit money
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        # Validate account
        if not self._is_valid_account(account):
            return False
        # Check sufficient funds
        if self.balance[account - 1] < money:
            return False
        # Withdraw money
        self.balance[account - 1] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
