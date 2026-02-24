#primary function file
from TimeStuff import when_updated
#make function to write onto the file
def add_to(file):
    with open(file, "a") as file:
        file.write(f'\n{input('Please input what you would like to add to your file: ')}')
        print(f"Updated on {when_updated()}.")

#make function to get word count of file
def word_count(file):
    count = 0
    try:
        with open(file, 'r') as file:
            content = []
            for line in file:
                content.append(line.strip())
    except:
        print("Ruh roh raggy")
    else:
        for line in content:
            for word in line.split():
                count += 1
    print(f"There are {count} words.")