class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Amount cannot be greater than balance.")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


ob_1 = BankAccount('123')
ob_2 = BankAccount('456', 100)

ob_1.deposit(200)
ob_2.deposit(50)
print(ob_1.balance)
print(ob_2.balance)
ob_1.withdraw(100)
ob_2.withdraw(100)
print(ob_1.balance)
print(ob_2.balance)
ob_1.withdraw(200)
ob_2.withdraw(200)
print(ob_1.balance)
print(ob_2.balance)