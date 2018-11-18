class CashMachine:
    def __init__(self):
        self.__bills = []
        self.broken = False

    @property
    def is_available(self):
        return bool(self.__bills)


    def put_money(self, bills):
        self.__bills.extend(bills)


    def withdraw_money(self, amount):
        bills = []
        for bill in sorted(self.__bills, revers=True):
            if sum(bills) + bill <= amount:
                bills.append(bill)

        if sum(bills) == amaunt:
            for bill in bills:
                self.__bills.remove(bill)
            return bills
        return []




def test_cash_machine_not_available():
    cash_machine = CashMachine()
    assert not cash_machine.is_available

def test_pcash_machine_is_available_after_put_money():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.is_available

def test_cash_machine_withdraw_money():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    cash_machine.withdraw_money(150) == [100, 50]