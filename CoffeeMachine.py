# Coffee Machine Project
import cofee_data
import os
import art
print("Welcome To Nestle Coffee Machine")
print(art.logo)
machineMoney = 0
cofResource = cofee_data.resources
water = cofResource["water"]
milk = cofResource["milk"]
coffee = cofResource["coffee"]
serviceContinue = True
while serviceContinue:
    service = input("“What would you like? (espresso/latte/cappuccino): ")
    if service == "report":
        print(f"Water: {water}")
        print(f"Milk: {milk}")
        print(f"Coffee: {coffee}")
        print(f"Money: ${machineMoney}")
    elif service == "espresso":
        if water >= 50 and coffee >= 18:
            print("Please insert coins")
            quarters = float(input("How many quarters?: "))
            dimes = float(input("How many dimes?: "))
            nickels = float(input("How many nickels?: "))
            pennies = float(input("How many pennies?: "))
            total = (quarters*0.25)+(dimes*0.1)+(nickels*0.05)+(pennies*0.01)
            if total < 1.5:
                print("Sorry that's not enough money. Money refunded.")
                continue
            change = total - 1.5
            change = round(change, 2)
            if change != 0:
                print(f"Here is ${change} in change.")
            print("Here is your espresso ☕ Enjoy!")
            water -= 50
            coffee -= 18
            machineMoney += 1.5
        else:
            if water < 50:
                print("Sorry there is not enough water.")
            else:
                print("Sorry there is not enough coffee.")
    elif service == "latte":
        if water >= 200 and milk >= 150 and coffee >= 24:
            print("Please insert coins")
            quarters = float(input("How many quarters?: "))
            dimes = float(input("How many dimes?: "))
            nickels = float(input("How many nickels?: "))
            pennies = float(input("How many pennies?: "))
            total = (quarters*0.25)+(dimes*0.1)+(nickels*0.05)+(pennies*0.01)
            if total < 2.5:
                print("Sorry that's not enough money. Money refunded.")
                continue
            change = total - 2.5
            change = round(change, 2)
            if change != 0:
                print(f"Here is ${change} in change.")
            print("Here is your latte ☕ Enjoy!")
            water -= 200
            milk -= 150
            coffee -= 24
            machineMoney += 2.5
        else:
            if water < 200:
                print(f"Sorry there is not enough water.")
            elif milk < 150:
                print(f"Sorry there is not enough milk.")
            else:
                print("Sorry there is not enough coffee.")
    elif service == "cappuccino":
        if water >= 250 and milk >= 100 and coffee >= 24:
            print("Please insert coins")
            quarters = float(input("How many quarters?: "))
            dimes = float(input("How many dimes?: "))
            nickels = float(input("How many nickels?: "))
            pennies = float(input("How many pennies?: "))
            total = (quarters*0.25)+(dimes*0.1)+(nickels*0.05)+(pennies*0.01)
            if total < 3.0:
                print("Sorry that's not enough money. Money refunded.")
                continue
            change = total - 3.0
            change = round(change, 2)
            if change != 0:
                print(f"Here is ${change} in change.")
            print("Here is your cappuccino ☕ Enjoy!")
            water -= 250
            milk -= 100
            coffee -= 24
            machineMoney += 3.0
        else:
            if water < 250:
                print(f"Sorry there is not enough water.")
            elif milk < 100:
                print(f"Sorry there is not enough milk.")
            else:
                print("Sorry there is not enough coffee.")
    elif service == "add":
        addMilk = int(input("How much milk would you like to add?: "))
        addWater = int(input("How much water would you like to add?: "))
        addCoffee = int(input("How much coffee would you like to add?: "))
        milk += addMilk
        water += addWater
        coffee += addCoffee
        print("Content Added Successfully")
    elif service == "off":
        serviceContinue = False
        print("Machine Turned Off Successfully!")
