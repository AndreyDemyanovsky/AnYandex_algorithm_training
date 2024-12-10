import sys

class Bank:
    def __init__(self):
        self.clients = {}

    def add_customer(self, name):
        self.clients[name] = 0
    
    def deposit_money(self, name, money):
        if not self.is_customer(name):
            self.add_customer(name)
        self.clients[name] += int(money)
    
    def is_customer(self, name):
        return name in self.clients

    def withdraw_money(self, name, money):
        if not self.is_customer(name):
            self.add_customer(name)
        self.clients[name] -=  int(money)

    def balance(self, name):
        if self.is_customer(name):
            return self.clients[name]
        return "ERROR"
    
    def transfer(self, name1, name2, money):
        self.withdraw_money(name1, int(money))
        self.deposit_money(name2, int(money))
    
    def income(self, p):
        for name in self.clients:
            money_customer = self.clients[name]
            if money_customer > 0:
                add_percent = money_customer * 0.01 * int(p)
                self.clients[name] += int(add_percent)

bank = Bank()

for data in sys.stdin:
    data = data.split()
    if data[0] == "DEPOSIT":
        bank.deposit_money(*data[1:])
    elif data[0] == "WITHDRAW":
        bank.withdraw_money(*data[1:])
    elif data[0] == "BALANCE":
        print(bank.balance(*data[1:]))
    elif data[0] == "TRANSFER":
        bank.transfer(*data[1:])
    elif data[0] == "INCOME":
        bank.income(*data[1:])


    