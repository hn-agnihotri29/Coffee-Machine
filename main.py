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
}


def is_resources_sufficient(order_ingredient):
    """Return True when order can, False if ingredient are insufficient"""
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print("Sorry there is not enough water.")
            return False
    return True


def process_coin():
    """Return the total calculated form coins inserted"""
    print("Please insert coins.")
    total = int(input("how many quarter:  ")) * 0.25
    total += int(input("how many dimes:  ")) * 0.1
    total += int(input("how many nickles:  ")) * 0.05
    total += int(input("how many pennies:  ")) * 0.01

    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money, Money refunded.")
        return False


def make_coffee(drink_name, order_ingredient):
    """Deduct required ingredient form the resources"""
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
        print(f"Here is your {drink_name} ☕")


profit = 0
is_On = True

while True:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        is_On = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
