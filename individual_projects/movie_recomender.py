import csv, time

#Make function to search for movie by given criteria
def recomend(preference, possibilities):
    with open("individual_projects/Movies list - Sheet1.csv", mode= 'r') as sample:
        reader = csv.reader(sample)

        for line in reader:

            score = 0

            #scores each movie based off of how many of the criteria are met.
            for choice in preference:
                if choice in str(line):
                    score += 1
                else:
                    pass
            
            #only recomend movies that follow all criteria
            if score == len(preference):
                possibilities.append(f"{line[0]}, directed by {line[1]}, genre: {line[2]}, rated {line[3]}, length of {line[4]} minutes, featuring {line[5]}")
            else:
                pass

    return possibilities

#make function to ask if they want to search by something
def ask_search(string):
    while True:
        yes_no = input(f"Do you want to search by {string}? Y/N: ")
        if yes_no.upper() == 'Y' or yes_no.upper() == 'N':
            break
        else:
            print("Invalid")
            continue
    return yes_no

#make function to ask what to search by
def ask_what(preference, item):
        preference.append(input(f"What {item} do you want to search by? ").lower().title().strip())
        

#make function for getting movie criteria of user
def criteria(preference):
    preference = []

    #check for genre preference
    if ask_search("genre").upper() == 'Y':
        ask_what(preference, "genre")
    else:
        pass
    
    #check for people preference
    if ask_search("people (actor / director)").upper() == 'Y':
        ask_what(preference, "people (actor / director)")
    else:
        pass

    return preference

#make function to output recomendations
def all_recomendations(possibilities):
    for i in possibilities:
        print(i)

#make function to read from whole movie list\
def read_all():
    with open("individual_projects/Movies list - Sheet1.csv", mode= 'r') as sample:
        reader = csv.reader(sample)

        for line in reader:
            if line[0] == 'Title':
                pass
            else:
                print(f"{line[0]}, directed by {line[1]}, genre: {line[2]}, rated {line[3]}, length of {line[4]} minutes, featuring {line[5]}")
                time.sleep(0.1)

#make function to run main program
def menu():
    while True:
        uinput = input("Would you like to 1: See all available movies, 2: Get a recomendation, 3: Leave? ")
        if uinput == '1':
            read_all()
        elif uinput == '2':
            preference = []
            possibilities = []
            preference = criteria(preference)
            possibilities = recomend(preference, possibilities)
            all_recomendations(possibilities)
        elif uinput == '3':
            break
        else:
            print("Invalid input.")
            continue

print("Welcome!")
menu()
print("Goodbye!")