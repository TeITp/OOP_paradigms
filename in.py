import random

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return amount
        else:
            return "Insufficient funds"

    def get_balance(self):
        return self.__balance


account = BankAccount("Andriy", 1000)

print(f"Початковий баланс: {account.get_balance()}")

for i in range(5):
    amount = random.randint(10, 500)

    if random.choice([True, False]):
        account.deposit(amount)
        print(f"Крок {i + 1}: Поповнено на {amount}. Поточний баланс: {account.get_balance()}")
    else:
        result = account.withdraw(amount)
        print(f"Крок {i + 1}: Спроба зняти {amount}. Результат: {result}. Баланс: {account.get_balance()}")

print(f"Кінцевий результат: {account.get_balance()}")