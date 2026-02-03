import csv

try:
    with open("notes/txt.txt", 'r') as file:
        content = []
        for line in file:
            content.append(line.strip())
except:
    print("Ruh roh raggy")
else:
    for line in content:
        print(line)

try:
    with open("notes/sample.csv", mode= 'r') as sample:
        reader = csv.reader(sample)
        users = []
        header = next(reader)
        for line in reader:
            users.append(
                {
                    header[0]: line[0],
                    header[1]: line[1]
                }
            )
except:
    print("Ruh roh raggy")
else:
    for user in users:
        print(user)