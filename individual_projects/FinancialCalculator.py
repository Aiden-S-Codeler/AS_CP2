#Financial Calculator AS 2nd
import time

#Make function to check if input is a number
def is_num(user_input):
    if user_input.isdigit() == True:
        return True
    else:
        return False

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
    while True:
        deposit = input("How much do you deposit at once?\n")
        if is_num(deposit) == True:
            deposit = int(deposit)
            break
        elif is_num(deposit) == False:
            print("Invalid choice.")
            continue
        else:
            print("Something broke.")
            continue

    #ask user for savings goal
    while True:
        goal = input("How much is your goal?\n")
        if is_num(goal) == True:
            goal = int(goal)
            break
        elif is_num(goal) == False:
            print("Invalid choice.")
            continue
        else:
            print("Something broke.")
            continue
    
    if frequency == "1":
        print(f"It will take you {goal/deposit} weeks to save up ${goal}")
        time.sleep(1)
    else:
        print(f"It will take you {goal/deposit} months to save up ${goal}")
        time.sleep(1)

#Make function for compound interest
def compound():
    #ask user for starting amount
    while True:
        start = input("What is your starting amount?\n")
        if is_num(start) == True:
            start = int(start)
            break
        elif is_num(start) == False:
            print("Invalid choice.")
            continue
        else:
            print("Something broke.")
            continue
    
    #ask user for interest rate
    while True:
        interest = input("What is the interest rate?\n")
        if is_num(interest) == True:
            interest = int(interest)
            break
        elif is_num(interest) == False:
            print("Invalid choice.")
            continue
        else:
            print("Something broke.")
            continue
    
    #ask user for how long they wait
    while True:
        itime = input("How many years will you let your money collect interest?\n")
        if is_num(itime) == True:
            itime = int(itime)
            break
        elif is_num(itime) == False:
            print("Invalid choice.")
            continue
        else:
            print("Something broke.")
            continue
    
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
    while True:
        category_count = input("How many budget categories do you have?\n")
        if is_num(category_count) == True:
            category_count = int(category_count)
            break
        elif is_num(category_count) == False:
            print("Invalid choice.")
            continue
        else:
            print("Something broke.")
            continue
    
    #make list to hold categories later
    categories = []
    
    #get new categories
    for i in range(category_count):
        category_add = input(f"What is budget category {i+1}?\n")
        categories.append(category_add)

    #get monthly income
    while True:
        income = input("What is your monthly income?\n")
        if is_num(income) == True:
            income = int(income)
            break
        elif is_num(income) == False:
            print("Invalid choice.")
            continue
        else:
            print("Something broke.")
            continue
    
    #make budget plan
    for c in categories:
        while True:
            spending = input(f"What percentage of your income goes to {c}?\n")
            if is_num(spending) == True:
                spending = int(spending)
                break
            elif is_num(spending) == False:
                print("Invalid choice.")
                continue
            else:
                print("Something broke.")
                continue
        print(f"{c} is {round((income/100)*spending, 2)}")
        time.sleep(1)

#sales calculator
def sales_price():
    #ask user for starting cost
    while True:
        start = input("What is your starting price?\n")
        if is_num(start) == True:
            start = int(start)
            break
        elif is_num(start) == False:
            print("Invalid choice.")
            continue
        else:
            print("Something broke.")
            continue
    
    #ask user for discount
    while True:
        discount = input("What is the discount?\n")
        if is_num(discount) == True:
            discount = int(discount)
            break
        elif is_num(discount) == False:
            print("Invalid choice.")
            continue
        else:
            print("Something broke.")
            continue
    
    #give final price
    print(f"The final price is ${start - ((start/100)*discount)}")
    time.sleep(1)

#tip calculator
def tip():
    #ask user for starting cost
    while True:
        start = input("What is your starting price?\n")
        if is_num(start) == True:
            start = int(start)
            break
        elif is_num(start) == False:
            print("Invalid choice.")
            continue
        else:
            print("Something broke.")
            continue
    
    #ask user for discount
    while True:
        tip = input("How much will you tip?\n")
        if is_num(tip) == True:
            tip = int(tip)
            break
        elif is_num(tip) == False:
            print("Invalid choice.")
            continue
        else:
            print("Something broke.")
            continue
    
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