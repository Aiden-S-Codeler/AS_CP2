#AS 2nd Word Counter, Main File
from CoolStuff import add_to, word_count, read_file

def main(file):
    while True:
        uinput = input("Would you like to 1: edit a file, 2: check the word count of a file, 3: read file, 4: exit ")
        if uinput == "1":
            add_to(file)
        elif uinput == "2":
            word_count(file)
        elif uinput == "3":
            read_file(file)
        elif uinput == "4":
            break
        else:
            print("Invalid option, try again")

print("Hello.")
main(input("What file would you like to edit: "))
print("Goodbye")