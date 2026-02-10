#AS 2nd personal library 2 electric boogaloo
import csv
#make a function to view all things in librarie
def view(library, exist):
    with open("individual_projects/personal_library2.csv", mode= 'r') as sample:
        reader = csv.reader(sample)
        print("Library includes:")
        for line in reader:
            if line[0] == 'Title':
                pass
            else:
                print(f"{line[0]}, written by {line[1]}, genre: {line[2]}")

#make function to add things to library
def add(library, exist):
    Author = input("Who wrote the book? ")
    if library:
        library[Author] = {input("What is the book title? ")}
        print(f"Added {library[Author]} by {Author} to library. If you had another book by that author, it was overwritten.")
    else:
        exist = True
        library[Author] = {input("What is the book title? ")}
        print(f"Added {library[Author]} by {Author} to library.")
    return(library, exist)

#make function for removing book
def remove(library, exist):
    if library:
        print("Your library includes:")
        for i in library:
            print(f"{library[i]} by {i}")
        while True:
            Author = input("What author would you like to remove? ")
            if Author in library:
                del library[Author]
                print(f"{Author} has been removed.")
                return(library)
                break
            else:
                print(f"There is no author under the name {Author}")
                continue
    else:
        print("You do not yet have a library")

#make function for searching
def search(library, exist):
    with open("individual_projects/personal_library2.csv", mode= 'r') as sample:
        reader = csv.reader(sample)
        uinput = input("Input title, author, or genre you would like to search for: ")
        for line in reader:
            if uinput.lower().title().strip() in line:
                print(f"{line[0]}, written by {line[1]}, genre: {line[2]}")
            else:
                pass

#make function for running code
def run(library, exist):
    while True:
        choice = input("Would you like to 1: search for a book, 2: add a book, 3: remove an author, 4: view your library, or 5: leave? Please enter the numeric value of your choice. ")
        if choice == "1":
            search(library, exist)
            continue
        elif choice == "2":
            library, exist = add(library, exist)
            continue
        elif choice == "3":
            library = remove(library, exist)
            continue
        elif choice == "4":
            view(library, exist)
            continue
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
            continue

print("Welcome to your library.")
run({}, False)
print("See you later!")