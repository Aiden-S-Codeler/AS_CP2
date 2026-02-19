#AS 2nd personal library 2 electric boogaloo
import csv
#make a function to view all things in librarie
def view():
    with open("individual_projects/personal_library2.csv", mode= 'r') as sample:
        reader = csv.reader(sample)
        print("Library includes:")
        for line in reader:
            if line[0] == 'Title':
                pass
            else:
                print(f"{line[0]}, written by {line[1]}, genre: {line[2]}, Pages: {line[3]}")

#make function to add things to library
def add():
    with open("individual_projects/personal_library2.csv", mode= 'a', newline= '') as sample:
        fieldnames = ['Title','Author','Genre','Length']
        writer = csv.DictWriter(sample, fieldnames=fieldnames)
        stuff = {'Title':input("What is the title? ").lower().title().strip(), 'Author':input("Who is the author? ").lower().title().strip(), 'Genre':input("What is the genre? ").lower().title().strip(), 'Length':input("What is the length? ").strip()}
        writer.writerow(stuff)
        
        
        
#make function for removing book
def remove():
    all = []
    uinput = input("What is the title you would like to remove? ").lower().title().strip()
    with open("individual_projects/personal_library2.csv", mode= 'r') as sample:
        reader = csv.reader(sample)
        for line in reader:
            if line[0] == 'Title':
                pass
            else:
                all.append({'Title':line[0] ,'Author':line[1] ,'Genre':line[2], 'Length':line[3]})
        for line in all:
            if line["Title"] == uinput:
                all.remove(line)
            else:
                pass
    with open("individual_projects/personal_library2.csv", mode= 'w', newline= '') as sample:
        fieldnames = ['Title','Author','Genre','Length']
        writer = csv.DictWriter(sample, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all)

#make function for searching
def search():
    with open("individual_projects/personal_library2.csv", mode= 'r') as sample:
        reader = csv.reader(sample)
        uinput = input("Input title, author, or genre you would like to search for: ")
        for line in reader:
            if uinput.lower().title().strip() in line:
                print(f"{line[0]}, written by {line[1]}, genre: {line[2]}, length: {line[3]}")
            else:
                pass

#make function for running code
def run():
    while True:
        choice = input("Would you like to 1: search for a book, 2: add a book, 3: remove a book, 4: view your library, or 5: leave? Please enter the numeric value of your choice. ")
        if choice == "1":
            search()
            continue
        elif choice == "2":
            add()
            continue
        elif choice == "3":
            remove()
            continue
        elif choice == "4":
            view()
            continue
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
            continue

print("Welcome to your library.")
run()
print("See you later!")
