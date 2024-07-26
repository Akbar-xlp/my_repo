# x = input()
# a = x[::-1]
# print(a)

from decimal import Decimal

class Client:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.amount = Decimal(0)

class Bank:
    def deposit(self, amount: Decimal, client: Client):
        client.amount += amount

    def payout(self, amount: Decimal, client: Client):
        client.amount -= amount
