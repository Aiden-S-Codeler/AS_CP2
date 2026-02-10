#AS 2nd file editing


#while True:
with open("notes/txt.txt", "a") as file:
    file.write("\nJilliano\n")
    file.write("Donatelliocho\n")
    file.write("Larry\n")
print("Done")
content = []
with open("notes/txt.txt", 'r+') as file:
    for line in file:
        content.append(line.strip())
    index = content.index('Jilliano')
    content[index] = "Torii"
    file.truncate(0)
    for name in content:
        file.write(name + "\n")
print('woah')

#import csv
#
#users = [{'username':'cosmic_voyager','favorite color':'indigo'},{'username':'tech_wizard','favorite color':'turquoise'},{'username':'nature_lover','favorite color':'emerald'},{'username':'bookworm42','favorite color':'maroon'}]
#
#with open("notes/silly.csv", 'a', newline='') as csvfile:
#    fieldnames = ['username', 'favorite color']
#    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#    writer.writeheader()
#    #writer.writerow(fieldnames)
#    writer.writerows(users)