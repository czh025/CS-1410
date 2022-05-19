"""
Project Name: Coffee Machine Project
Author: Zhihui Chen
Due Date: 06/02/2022
Course: CS1410-X01

Put your description here, lessons learned here, and any other information someone using your
program would need to know to make it run.
"""


class CoffeeMachine:
    products = (
        ("black", 35, "coffee"),
        ("white", 35, "coffee", "creamer"),
        ("sweet", 35, "coffee", "sugar"),
        ("white & sweet", 35, "coffee", "sugar", "creamer"),
        ("bouillon", 25, "bouillonPowder")
    )

    def __init__(self):
        self.cashBox = CashBox()
        self.selector = Selector(self.cashBox, CoffeeMachine.products)

    def oneAction(self):
        print("")
        print("_" * 40)
        print("PRODUCT LIST: all 35 cents, except bouillon (25 cents)")
        print("1=black, 2=white, 3=sweet, 4=while & sweet, 5=bouillon")
        print("Sample commands: insert 25, select 1.")

        user_input = input("Your command: \u001b[1m").lower()
        print('\u001b[0m', end='')

        if "insert" in user_input and " " in user_input:
            insert_cash = user_input.split()[1]
            self.cashBox.deposit(insert_cash)
        elif "select" in user_input:
            item_index = int(user_input.split()[1])
            self.selector.select(item_index)
        elif user_input == "cancel":
            self.cashBox.returnCoins()
        elif user_input == "quit":
            return False
        else:
            print("Invalid command.")
        return True

    def totalCash(self):
        return self.cashBox.total()


class CashBox:
    def __init__(self):
        self.__credit = 0
        self.__totalReceived = 0

    def deposit(self, amount):
        """
        amount: int
        """
        if amount not in ("50", "25", "10", "5"):
            print("INPUT ERROR >>>")
            print("We only take half-dollars, quarters, dimes, and nickels.")
            print("Coin(s) returned")
            return
        self.__credit += int(amount)
        print(f"Depositing {amount}. You have {self.__credit} cents credit.")

    def returnCoins(self):
        if self.__credit != 0:
            print(f"Returning {self.__credit} cents.")
            self.__credit = 0

    def haveYou(self, amount):
        """
        return bool
        """
        return self.__credit >= amount

    def deduct(self, amount):
        self.__credit -= amount
        self.__totalReceived += amount

    def total(self):
        """
        return int
        """
        return self.__totalReceived


class Selector:
    def __init__(self, cash_box, products):
        self.__cashBox = cash_box
        self.__products = products

    def select(self, choiceIndex):
        """
        choiceIndex: int
        """
        if choiceIndex > 5 or choiceIndex < 0:
            print("Invalid choice.")
            return
        p = Product(self.__products[choiceIndex - 1][0], self.__products[choiceIndex - 1][1],
                    self.__products[choiceIndex - 1][2:])
        drink_price = p.getPrice()
        is_enough_credit = self.__cashBox.haveYou(drink_price)
        if is_enough_credit:
            p.make()
            self.__cashBox.deduct(drink_price)
            self.__cashBox.returnCoins()
        else:
            print("Sorry. Not enough money deposited.")


class Product:
    def __init__(self, name, price, recipe):
        self.__name = name
        self.__price = price
        self.__recipe = recipe

    def getPrice(self):
        """
        return int
        """
        return self.__price

    def make(self):
        """
        Dispenses the drink
        """
        print(f"Making {self.__name}:")
        print("      Dispensing cup")
        for item in self.__recipe:
            print(f"      Dispensing {item}")
        print("      Dispensing water")


def main():
    """
    Program starts here.
    """
    m = CoffeeMachine()
    while m.oneAction():
        pass
    total = m.totalCash()
    print(f"Total cash: ${total / 100:.2f}")


if __name__ == "__main__":
    main()
