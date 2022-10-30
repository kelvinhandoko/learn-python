from re import I


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {"water": 300, "milk": 200, "coffee": 50, "money": 0}

coins = {"quaters": 0.25, "dimes": 0.1, "nickles": 0.05, "penny": 0.01}


machine_start = True


def check_ingridient(menu):
    for item in menu["ingredients"]:
        if menu["ingredients"][item] > resources[item]:
            print(f"sorry we run out {item}")
            return False
    return True


def check_balance(quarter, dimes, nickle, penny, menu):
    money = coins["quaters"] * quarter + coins["dimes"] * dimes + coins["nickles"] * nickle + coins["penny"] * penny
    balance = money - menu.get("cost")
    if balance > 0:
        global resources
        print(f"Here is ${round(balance,2)} in change.")
        for item in resources:
            if item != "money":
                resources[item] -= menu["ingredients"].get(item, 0)
            else:
                resources[item] += menu.get("cost")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


while machine_start:
    user = input("hi! what would you like? (espresso / latte / cappuccino) ")
    if user == "off":
        machine_start = False
    elif user == "report":
        for key, value in resources.items():
            if key == "money":
                print(f"{key} : ${value}")
            else:
                print(f"{key} : {value}")
    else:
        if check_ingridient(MENU[user]):
            many_quarter = int(input("how many quarter ? "))
            many_dimes = int(input("how many dimes ? "))
            many_nikle = int(input("how many nikle ? "))
            many_penny = int(input("how many penny ? "))
            if check_balance(many_quarter, many_dimes, many_nikle, many_penny, MENU[user]):
                print(f"here your {user}. enjoy!")
        else:
            machine_start = False
