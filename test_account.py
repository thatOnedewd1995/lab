from account import *

class Test:
    def setup_method(self):
        self.p1 = Account('Jimmy', 50)

    def test_init(self):
        assert self.p1.get_name() == 'Jimmy'
        assert self.p1.get_balance() == 50

    def test_deposit(self):
        assert self.p1.deposit(30) is True
        assert self.p1.get_balance() == 80

        assert self.p1.deposit(0) is False
        assert self.p1.get_balance() == 80

        assert self.p1.deposit(-30) is False
        assert self.p1.get_balance() == 80

    def test_withdraw(self):
        assert self.p1.withdraw(30) is True
        assert self.p1.get_balance() == 20

        assert self.p1.deposit(0) is False
        assert self.p1.get_balance() == 20

        assert self.p1.withdraw(-30) is False
        assert self.p1.get_balance() == 20

        assert self.p1.withdraw(-60) is False
        assert self.p1.get_balance() == 20