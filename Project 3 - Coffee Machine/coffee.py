"""
Project Name: Coffee Machine Project
Author: Zhihui Chen
Due Date: 06/02/2022
Course: CS1410-X01

Put your description here, lessons learned here, and any other information someone using your
program would need to know to make it run.
"""


class CoffeeMachine:
    def __init__(self):
        self.__cashBox = 0
        self.__selector = None


    def oneAction(self):
        print("PRODUCT LIST: all 35 cents, except bouillon (25 cents)")
        print("1=black, 2=white, 3=sweet, 4=while & sweet, 5=bouillon")
        print("Sample commands: insert 25, select 1.")

        user_input = input("Your command: \u001b[1m").lower()
        print('\u001b[0m', end='')

        if "insert" in user_input:
            insert_cash = user_input.split()[1]
            if insert_cash == "50" or insert_cash == "25" or insert_cash == "10" or insert_cash == "5":
                self.__cashBox += int(insert_cash)
                print(f"Depositing {insert_cash}. You have {self.__cashBox} cents credit.")
                self.totalCash()
            else:
                print("INPUT ERROR >>>")
                print("We only take half-dollars, quarters, dimes, and nickels.")
                print("Coin(s) returned")
                return True
        elif "select" in user_input:
            item_index = int(user_input.split()[1])
            s = Selector(self.__cashBox)
            s.select(item_index)
        elif user_input == "cancel":
            print("cancel")
        elif user_input == "quit":
            return False
        else:
            print("Invalid command.")
        return True


    def totalCash(self):
        b = CashBox()
        b.deposit(self.__cashBox)


class CashBox:
    def __init__(self):
        self.__credit = 0
        self.__totalReceived = 0


    def deposit(self, amount):
        """
        amount: int
        """
        self.__credit += amount
        self.__totalReceived += amount
        print("999aaa", self.__totalReceived, self.__credit)


    def returnCoins(self):
        print(f"Returning {self.__credit} cents.")


    def haveYou(self, amount):
        """
        determine if user have enough money
        return bool
        """
        print(self.__credit, self.__totalReceived, amount)
        return True if self.__credit >= amount else False


    def deduct(self, amount):
        print("sdasddfasf", self.__totalReceived, self.__credit)
        self.__credit -= amount


    def total(self):
        """
        return int
        """
        print("here", self.__credit, self.__totalReceived)
        pass


class Selector:
    def __init__(self, cashBox):
        self.__cashBox = cashBox
        self.__products = ["black", "white", "sweet", "white & sweet", "bouillon"]


    def select(self, choiceIndex):
        """
        choiceIndex: int
        """
        p = Product(self.__products[choiceIndex - 1], self.__cashBox)
        drink_price = p.getPrice()
        b = CashBox()
        is_enough_credit = b.haveYou(drink_price)
        if is_enough_credit:
            p.make()
            b.deduct(drink_price)
            b.returnCoins()
        else:
            print("Sorry. Not enough money deposited.")


class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
        self.__recipe = []


    def getPrice(self):
        """
        Abstraction of the drink
        Responsible for knowing its price and recipe

        return int
        """
        if self.__name == "bouillon":
            self.__recipe.append("cup")
            self.__recipe.append("bouillonPowder")
            self.__recipe.append("water")
            return 25
        else:
            self.__recipe.append("cup")
            self.__recipe.append("coffee")
            if self.__name == "black":
                pass
            elif self.__name == "white":
                self.__recipe.append("creamer")
            elif self.__name == "sweet":
                self.__recipe.append("sugar")
            else:
                self.__recipe.append("sugar")
                self.__recipe.append("creamer")
            self.__recipe.append("water")
            return 35


    def make(self):
        """
        Dispenses the drink
        """
        print(f"Making {self.__name}")
        for item in self.__recipe:
            print(f"      Dispensing {item}")


def main():
    """
    Program starts here.
    """
    m = CoffeeMachine()
    while m.oneAction():
        print("")
    total = m.totalCash()
    print(f"Total cash: ${total/100:.2f}")


if __name__ == "__main__":
    main()
