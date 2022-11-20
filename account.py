class Account:
    def __init__(self, name, balance=0) -> None:
        self.__account_balance = balance
        self.__account_name = name

    def deposit(self, amount) -> bool:
        if amount <= 0:
            return False
        else:
            self.__account_balance = self.__account_balance + amount
            return True

    def withdraw(self, amount) -> bool:
        if amount <= 0:
            return False
        elif amount > self.__account_balance:
            return False
        else:
            self.__account_balance = self.__account_balance - amount
            return True

    def get_balance(self) -> float:
        return self.__account_balance

    def get_name(self) -> str:
        return self.__account_name