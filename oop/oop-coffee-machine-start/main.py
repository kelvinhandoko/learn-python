from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
is_on = True
while is_on:
    choice = menu.get_items()
    user = input(f"What would you like? ({choice}) ")
    if user == "report":
        coffee_maker.report()
        money_machine.report()
    elif user == "off":
        is_on = False
    else:
        drink = menu.find_drink(user)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
