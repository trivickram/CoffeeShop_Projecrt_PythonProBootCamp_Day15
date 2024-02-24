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
    "water": 900,
    "milk": 500,
    "coffee": 300,
}
profit = 0
Run=True
def amount():
    print("Please enter coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return round(total,2)
ret=0
def report():
    print("water", ":", resources["water"], "ml\n""milk", ":", resources["milk"], "ml\n""coffee", ":",resources["coffee"], "g\n","Money : $",profit)
def Machine(user):
    global profit
    global ret
    if user=="espresso":


        if resources["water"]<50:
            print("Sorry there is not enough water.")
            return
        elif resources["coffee"]<18:
            print("Sorry there is not enough coffee.")
            return
        espresso = amount()
        if espresso>1.5 and resources["water"]>=50 and resources["coffee"]>=18:
            print(f"Here is ${espresso} in change")
            resources["water"]=resources["water"]-50
            resources["coffee"]=resources["coffee"]-18
            print("Here is your espresso☕.Enjoy!")
            profit = profit + 1.5
            ret=espresso-1.5
        elif espresso<1.5:
            print("Sorry that's not enough money. Money refunded.")
            return
    elif user=="latte":


        if resources["water"]<200:
            print("Sorry there is not enough water.")
            return
        elif resources["coffee"]<24:
            print("Sorry there is not enough coffee.")
            return
        elif resources["milk"]<150:
            print("Sorry there is not enough milk.")
            return
        latte = amount()
        if latte>2.5 and resources["water"]>=200 and resources["coffee"]>=24 and resources["milk"]>=150:
            print(f"Here is ${latte} in change")
            profit=profit+2.5
            resources["water"]=resources["water"]-200
            resources["coffee"]=resources["coffee"]-24
            resources["milk"]=resources["milk"]-150
            print("Here is your latte☕.Enjoy!")
            ret=latte-2.5
        elif latte<2.5:
            print("Sorry that's not enough money. Money refunded.")
            return
    elif user=="cappuccino":

        if resources["water"]<300:
            print("Sorry there is not enough water.")
            return
        elif resources["coffee"]<100:
            print("Sorry there is not enough coffee.")
            return
        elif resources["milk"]<200:
            print("Sorry there is not enough milk.")
            return
        cappuccino = amount()
        if cappuccino>3 and resources["water"]>=300 and resources["coffee"]>=100 and resources["milk"]>=200:
            print(f"Here is ${cappuccino} in change")
            profit=profit+3
            resources["water"]=resources["water"]-250
            resources["coffee"]=resources["coffee"]-24
            resources["milk"]=resources["milk"]-100
            print("Here is your cappuccino☕.Enjoy!")
            ret=cappuccino-3.0
        elif cappuccino<3.0:
            print("Sorry that's not enough money. Money refunded.")
            return


while Run:
    user = input("What would you like? (espresso/latte/cappuccino):")
    if user=="off":
        Run=False
    elif user=="report":
        report()
    else :
        Machine(user)








