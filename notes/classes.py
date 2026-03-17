#AS 2nd classes notes

#ex 1
class Dog:
    def __init__(self, name, breed, age):
        self.name = name.capitalize()
        self.breed = breed.title()
        self.age = age

    def __str__(self):
        return f"Name: {self.name}\nBreed: {self.breed}\nAge: {self.age}\n"

doug = Dog('Doug', "Golden Retreiver", 3)
pongo = Dog("Pongo", "Dalmation", 8)

print(doug)
print(pongo)