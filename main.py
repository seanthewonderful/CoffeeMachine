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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

# print(MENU["espresso"]["ingredients"])


is_on = True


def check_resources(ingredients):
    if ingredients["water"] > resources["water"] or ingredients["milk"] > resources["milk"] or ingredients["coffee"] > resources["coffee"]:
        return False
    else:
        return True


def order_esp():
    print("Please insert coins-")
    q = int(input("How many quarters: "))
    d = int(input("How many dimes: "))
    n = int(input("How many nickels: "))
    p = int(input("How many pennies: "))
    cost = MENU["espresso"]["cost"]
    coin_input = (q * 0.25) + (d * 0.1) + (n * 0.05) + (p * 0.01)
    if coin_input >= cost:
        resources["money"] += cost
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
        print(f"Here is your espresso.\nYour change is ${coin_input - cost}")
    else:
        print("Sorry, that wasn't enough money")


def order_lat():
    print("Please insert coins-")
    q = int(input("How many quarters: "))
    d = int(input("How many dimes: "))
    n = int(input("How many nickels: "))
    p = int(input("How many pennies: "))
    cost = MENU["latte"]["cost"]
    coin_input = round((q * 0.25) + (d * 0.1) + (n * 0.05) + (p * 0.01), 2)
    if coin_input >= cost:
        resources["money"] += cost
        resources["water"] -= MENU["latte"]["ingredients"]["water"]
        resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
        print(f"Here is your Latte.\nYour change is ${round(coin_input - cost, 2)}")
    else:
        print("Sorry, that wasn't enough money it was only", coin_input)


def order_cap():
    print("Please insert coins-")
    q = int(input("How many quarters: "))
    d = int(input("How many dimes: "))
    n = int(input("How many nickels: "))
    p = int(input("How many pennies: "))
    cost = MENU["cappuccino"]["cost"]
    coin_input = (q * 0.25) + (d * 0.1) + (n * 0.05) + (p * 0.01)
    if coin_input >= cost:
        resources["money"] += cost
        resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
        print(f"Here is your cappuccino.\nYour change is ${coin_input - cost}")
    else:
        print("Sorry, that wasn't enough money")


def generate_report():
    print(f"""
Water: {resources["water"]}
Milk: {resources["milk"]}
Coffee: {resources["coffee"]}
Money: ${resources["money"]}
""")


while is_on:
    inp = input("What would you like? (espresso/latte/cappuccino): ")
    if inp == "espresso":
        if check_resources(MENU["espresso"]["ingredients"]):
            order_esp()
        else:
            print(f"Sorry there is not enough resources")
    elif inp == "latte":
        if check_resources(MENU["latte"]["ingredients"]):
            order_lat()
        else:
            print(f"Sorry there is not enough resources")
    elif inp == "cappuccino":
        if check_resources(MENU["cappuccino"]["ingredients"]):
            order_cap()
        else:
            print(f"Sorry there is not enough resources")
    elif inp == "report":
        generate_report()
    elif inp == "off":
        is_on = False
    else:
        if input("Coffee Machine powering down. Would you like to restart? y or n: ") == "n":
            is_on = False



# TODO: 1. "report" entered by user return a report that shows current resource values
# TODO: 2. input - what would you like? espresso, latte, cappuccino, report, off,