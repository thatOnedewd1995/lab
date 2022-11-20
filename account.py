class Account:
    """
    A class that tracks someone's account information
    """
    def __init__(self, name, balance=0) -> None:
        """
        Constructor to create initial state of a person account.
        :param name: Person's first name.
        :param balance: Person's account balance in dollars.
        """
        self.__account_balance = balance
        self.__account_name = name

    def deposit(self, amount) -> bool:
        """
        Method for depositing money into an account.
        :param amount: Amount of the deposit.
        :return: Boolean value with status of deposit.
        """
        if amount <= 0:
            return False
        else:
            self.__account_balance = self.__account_balance + amount
            return True

    def withdraw(self, amount) -> bool:
        """
        Method for withdrawing money from an account.
        :param amount: Amount of the withdrawal.
        :return: Boolean value with status of withdrawal.
        """
        if amount <= 0:
            return False
        elif amount > self.__account_balance:
            return False
        else:
            self.__account_balance = self.__account_balance - amount
            return True

    def get_balance(self) -> float:
        """
        Method for getting account balance.
        :return: Account balance.
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Method for getting account name.
        :return: Account name.
        """
        return self.__account_name