class Account:
    account_name = " "
    account_balance = 0
    def __init__(self,name, balance):
        self.__account_balance = balance
        self.__account_name = name



    def deposit(self,amount, balance):
        self.__amount = amount
        self.__account_balance = balance
        if amount <= 0:
            return False
        else:
            self.__account_balance = balance + amount
            return True


    def withdraw(self,amount, balance):
        self.__amount = amount
        self.__account_balance = balance
        if amount <= 0:
            return False
        else:
            aself.__account_balance = balance - amount
            return True


    def get_balance(self):
        return account_balance


    def get_name(self):
        return account_name

