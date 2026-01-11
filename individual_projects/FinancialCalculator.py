#Financial Calculator AS 2nd
import time

#Make function to check if input is a number
def is_num(user_input):
    if user_input.isdigit() == True:
        return True
    else:
        return False

#make function to check if is_num is true and then make input number
def check(uinput):
    while True:
        if is_num(uinput) == True:
            uinput = int(uinput)
            break
        elif is_num(uinput) == False:
            uinput = input("Invalid choice. Try again.\n")
            continue
        else:
            print("Something broke.")
            continue
    return uinput

#Make function to see how long it takes to save for a specific monetary amount
def savings():
    #ask how often user deposits
    while True:
        frequency = input("How often do you deposit? 1:Weekly  2:Monthly\n")
        if frequency == "1" or frequency == "2":
            break
        else:
            print("Invalid choice.")
            continue
    
    #ask much user deposits
    deposit = input("How much do you deposit at once?\n")
    check(deposit)
    deposit = check(deposit)

    #ask user for savings goal
    goal = input("How much is your goal?\n")
    check(goal)
    goal = check(goal)
    
    if frequency == "1":
        print(f"It will take you {goal/deposit} weeks to save up ${goal}")
        time.sleep(1)
    else:
        print(f"It will take you {goal/deposit} months to save up ${goal}")
        time.sleep(1)

#Make function for compound interest
def compound():
    #ask user for starting amount
    start = input("What is your starting amount?\n")
    check(start)
    start = check(start)
    
    #ask user for interest rate
    interest = input("What is the interest rate?\n")
    
    
    #ask user for how long they wait
    itime = input("How many years will you let your money collect interest?\n")
    check(itime)
    itime = check(itime)
    
    #make inner function to do compund interest
    def biggering(start, interest, itime):
        for i in range(itime):
            start += (start/100)*interest
            start = round(start,)
        return start
    
    print(biggering(start, interest, itime))
    time.sleep(1)

#make function for budgeting
def budget():

    #ask for amount of categories
    category_count = input("How many budget categories do you have?\n")
    check(category_count)
    category_count = check(category_count)
    
    #make list to hold categories later
    categories = []
    
    #get new categories
    for i in range(category_count):
        category_add = input(f"What is budget category {i+1}?\n")
        categories.append(category_add)

    #get monthly income
    income = input("What is your monthly income?\n")
    check(income)
    income = check(income)
    
    #make budget plan
    for c in categories:
        spending = input(f"What percentage of your income goes to {c}?\n")
        check(spending)
        spending = check(spending)
        print(f"{c} is {round((income/100)*spending, 2)}")
        time.sleep(1)

#sales calculator
def sales_price():
    #ask user for starting cost
    start = input("What is your starting price?\n")
    check(start)
    start = check(start)
    
    #ask user for discount:
    discount = input("What is the discount?\n")
    check(discount)
    discount = check(discount)
    
    #give final price
    print(f"The final price is ${start - ((start/100)*discount)}")
    time.sleep(1)

#tip calculator
def tip():
    #ask user for starting cost
    start = input("What is your starting price?\n")
    check(start)
    start = check(start)
    
    #ask user for discount
    tip = input("How much will you tip?\n")
    check(tip)
    tip = check(tip)
    
    #give final price
    print(f"The tip is {(start/100)*tip} and the final price is ${start + ((start/100)*tip)}")
    time.sleep(1)

print("Welcome to the financial calulator")
while True:
    uchoice = input("Would you like to:\n1: Calculate how long it will take to save for a goal\n2: Calculate compound interest\n3: Make a budget\n4: Calculate the pre-tax sales price\n5: Calculate a tip\n6: leave\nplease enter the numeric value for your choice: ")
    if uchoice == "1":
        savings()
        pass
    elif uchoice == "2":
        compound()
        pass
    elif uchoice == "3":
        budget()
        pass
    elif uchoice == "4":
        sales_price()
        pass
    elif uchoice == "5":
        tip()
        pass
    elif uchoice == "6":
        print("See you soon!")
        time.sleep(1.0)
        break
    else:
        print("Invalid choice")
        continue