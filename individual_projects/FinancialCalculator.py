#Financial Calculator AS 2nd

#Make function to get percentage of a number
def percent(num, perc):
    final_number = (num/100)*perc
    return final_number

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
        frequency = input("How long are you saving? 1:Weekly  2:Monthly\n")
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
        goal = input("How much do you goal at once?\n")
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
    else:
        print(f"It will take you {goal/deposit} months to save up ${goal}")

#Make function for compound interest
def compound():
    #ask user for starting amount
    while True:
        start = input("What is your starting amount?\n")