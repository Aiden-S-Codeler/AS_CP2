#AS 2nd personal library

#make a function to view all things in libraries
def view(library, exist):
    if exist == True:
        print("Your library includes:")
        for i in library:
            print(f"{library[i]} by {i}")
    else:
        print("You do not yet have a library")

#make function to add things to library
def add(library, exist):
    Author = input("")
    if exist == True:
        