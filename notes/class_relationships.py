#AS 2nd inheritance

#Parent Class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Vroom")

#Child Classes
#Composition
class Engine:
    def __init__(self, model):
        self.model = model
    
    def __str__(self):
        return self.model

class Car(Vehicle):
    def __init__(self, brand, model, engine):
        super().__init__(brand, model, engine)
        self.engine = Engine('v8')

class Boat(Vehicle):
    def move(self):
        print("Splash")

class Plane(Vehicle):
    def move(self):
        print("Swoosh")

car = Car('Ford', 'Mustang')
boat = Boat('Kowazaki', 'Big')
plane = Plane('Boeing', '747')

for i in (car, boat, plane):
    print(i.brand)
    print(i.model)
    i.move()
    print('')
print(Car.engine)

#Aggregete (Has A)
class Library:
    def __init__(self, name, catalog = []):
        self.name = name
        self.catalog = catalog
    
    def add_book(self, book):
        self.catalog.append(book)
    
    def remove_book(self, book):
        if book in self.catalog:
            self.catalog.pop(book)
        else:
            print('Loser')
    
    def view_catalog(self):
        for book in self.catalog:
            print(book)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

lib = Library("Provo Library")
book = Book("Inkheart", "Cornilia Funke")

lib.add_book(Book("Skyward", "Brandon Sanderson"))
lib.add_book(Book("The Hobbit", "J. R. R. Tolkien"))
lib.add_book(Book("The Last Battle", "C.S. Lewis"))
lib.add_book(Book("The Great Hunt", "Robert Jordan"))

lib.view_catalog()