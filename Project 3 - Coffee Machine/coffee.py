"""
Project Name: Coffee Machine Project
Author: Zhihui Chen
Due Date: 06/02/2022
Course: CS1410-X01

This program accepts insert, select, cancel, and quit command.
The user can use these command to buy coffee or bouillon.
If user enter quit command, the program will end.

Through this project I learned how to use classes and understand UML diagrams
"""


class CoffeeMachine:
    """
    PRODUCTS: a list of products, should not be changed

    one_action: accept user's input until user enter quit
    total_cash: return total cash that user spend
    """
    PRODUCTS = (
        ("black", 35, "coffee"),
        ("white", 35, "coffee", "creamer"),
        ("sweet", 35, "coffee", "sugar"),
        ("white & sweet", 35, "coffee", "sugar", "creamer"),
        ("bouillon", 25, "bouillonPowder")
    )

    def __init__(self):
        self.cashBox = CashBox()
        self.selector = Selector(self.cashBox, CoffeeMachine.PRODUCTS)

    def one_action(self):
        """
        repeat help
        execute different methods depending on the user's input
        """
        print("")
        print("_" * 40)
        print("PRODUCT LIST: all 35 cents, except bouillon (25 cents)")
        print("1=black, 2=white, 3=sweet, 4=while & sweet, 5=bouillon")
        print("Sample commands: insert 25, select 1.")

        user_input = input("Your command: \u001b[1m").lower()
        print('\u001b[0m', end='')

        if "insert" in user_input and " " in user_input:
            if user_input.split()[1].isdigit():
                self.cashBox.deposit(int(user_input.split()[1]))
            else:
                print("INVALID AMOUNT >>>")
                print("We only take half-dollars, quarters, dimes, and nickels.")
        elif "select" in user_input:
            if user_input.split()[1].isdigit():
                item_index = int(user_input.split()[1])
                self.selector.select(item_index)
            else:
                print("Invalid choice.")
        elif user_input == "cancel":
            self.cashBox.return_coins()
        elif user_input == "quit":
            return False
        else:
            print("Invalid command.")
        return True

    def total_cash(self):
        """
        return int
        total cash that user spent
        """
        return self.cashBox.total()


class CashBox:
    """
    instance attributes:
    credit: user's remaining cash
    totalReceived: total cash spent by users

    instance method:
    deposit: deposit cash, only accept 50,25,10,5
    return_coins: refund of the remaining cash
    have_you: return True or False, determine if the user has enough cash to buy the product
    deduct: Reduce user balance after purchase
    total: return total cash that user spend
    """

    def __init__(self):
        self.__credit = 0
        self.__total_received = 0

    def deposit(self, amount):
        """
        amount: int
        """
        if amount not in (50, 25, 10, 5):
            print("INVALID AMOUNT >>>")
            print("We only take half-dollars, quarters, dimes, and nickels.")
            return
        self.__credit += amount
        print(f"Depositing {amount} cents. You have {self.__credit} cents credit.")

    def return_coins(self):
        """
        If the user's credit is greater than 0,
            the credit will be returned and the credit will be cleared
        """
        if self.__credit != 0:
            print(f"Returning {self.__credit} cents.")
            self.__credit = 0

    def have_you(self, amount):
        """
        return bool
        """
        return self.__credit >= amount

    def deduct(self, amount):
        """
        subtract the amount left by the user
        add the amount spent to total_received
        """
        self.__credit -= amount
        self.__total_received += amount

    def total(self):
        """
        return int
        """
        return self.__total_received


class Selector:
    """
    select: If the user enters the correct product,
        the information about the product that the user needs is extracted from the products
    """

    def __init__(self, cash_box, products):
        self.__cash_box = cash_box
        self.__products = products

    def select(self, choice_index):
        """
        __products[0]: product's name
        __products[1]: product's price
        __products[2:]: product's materials
        """
        if choice_index > 5 or choice_index < 0:
            print("Invalid choice.")
            return
        product_detail = Product(self.__products[choice_index - 1][0],
                                 self.__products[choice_index - 1][1],
                                 self.__products[choice_index - 1][2:])
        drink_price = product_detail.get_price()
        is_enough_credit = self.__cash_box.have_you(drink_price)
        if is_enough_credit:
            product_detail.make()
            self.__cash_box.deduct(drink_price)
            self.__cash_box.return_coins()
        else:
            print("Sorry. Not enough money deposited.")


class Product:
    """
    get_price: return price of product which user chose
    make: start to make drink
    """

    def __init__(self, name, price, recipe):
        self.__name = name
        self.__price = price
        self.__recipe = recipe

    def get_price(self):
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
    while m.one_action():
        pass
    total = m.total_cash()
    print(f"Total cash received: ${total / 100:.2f}")


if __name__ == "__main__":
    main()
