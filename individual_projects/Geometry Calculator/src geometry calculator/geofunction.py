#AS 2nd Geometry Claculator

cir_count = 1
tri_count = 1
squ_count = 1
rec_count = 1


class Square:
    def __init__(self, side_len, area= 0, perimeter= 0, name= f"Square{squ_count}"):
        self.side_len = side_len
        self.area = self.side_len * self.side_len
        self.perimeter = self.side_len * 4
        self.name = name

    def __str__(self):
        return f"Shape: Square\nSide Length: {self.side_len}\nArea: {self.area}\nPerimeter: {self.perimeter}\n"

class Rectangle:
    def __init__(self, side_len, base_len, area= 0, perimeter= 0, name= f"Rectangle{rec_count}"):
        self.side_len = side_len
        self.base_len = base_len
        self.area = self.side_len * self.base_len
        self.perimeter = (self.side_len * 2) + (self.base_len * 2)
        self.name = name

    def __str__(self):
        return f"Shape: Rectangle\nSide Length: {self.side_len}\nBase Length: {self.base_len}\nArea: {self.area}\nPerimeter: {self.perimeter}\n"

class Triangle:
    def __init__(self, height, base_len, area= 0, perimeter= 0, name= f"Triangle{tri_count}"):
        self.height = height
        self.base_len = base_len
        self.area = (self.height * self.base_len)/2
        self.perimeter = self.base_len * 3
        self.name = name

    def __str__(self):
        return f"Shape: Triangle\nHeight: {self.height}\nBase Length: {self.base_len}\nArea: {self.area}\nPerimeter: {self.perimeter}\n"

class Circle:
    def __init__(self, radius, diameter= 0, area= 0, circumference= 0, name= f"Circle{cir_count}"):
        self.radius = radius
        self.diameter = radius * 2
        self.area = round((3.1415926535 * (radius * radius)), 2)
        self.circumference = round((2 * 3.1415926535 * radius),2)
        self.name = name

    def __str__(self):
        return f"Shape: Circle\nRadius: {self.radius}\nDiameter: {self.diameter}\nArea: {self.area}\nCircumference: {self.circumference}\n"

def input_check(uinput):
    try:
        uinput = float(uinput)
    except:
        return False
    
    if uinput > 0:
        return True
    else:
        return False
    
def int_input(measure):
    while True:
        try:
            uinput = int(input(f"What do you want your {measure} to be? "))
            break
        except:
            print("Invalic option.")
            continue
    return uinput

def compare(shape1, shape2):
    try:
        if shape1.area > shape2.area:
            print(f"{shape1.name} has a larger area than {shape2.name}.")
        elif shape1.area < shape2.area:
            print(f"{shape2.name} has a larger area than {shape1.name}.")
        elif shape1.area == shape2.area:
            print(f"{shape1.name} and {shape2.name} have the same area.")
    except:
        pass

    try:
        if shape1.perimeter > shape2.perimeter:
            print(f"{shape1.name} has a larger perimeter than {shape2.name}.")
        elif shape1.perimeter < shape2.perimeter:
            print(f"{shape2.name} has a larger perimeter than {shape1.name}.")
        elif shape1.perimeter == shape2.perimeter:
            print(f"{shape1.name} and {shape2.name} have the same perimeter.")
    except:
        pass

def view(library):
    for x in range(len(library)):
        print(f"{x+1}: {library[x].name}")

def specify(library, this):
    print("Your options are:")
    view(library)
    while True:
        uinput = input(f"\nWhat is your {this} shape? ")
        if input_check(uinput) == True:
            uinput = int(uinput)
        else:
            print('Invalid choice.')
            continue
        if uinput - 1 < len(library):
            break
        else:
            print('Invalid choice.')
            continue
    
    return library[uinput-1]

def edit(library):
    print("Your options are:")
    view(library)
    while True:
        uinput = input("\nWhat shape would you like to edit? ")
        if input_check(uinput) == True:
            uinput = int(uinput)
        else:
            print('Invalid choice.')
            continue
        if uinput - 1 < len(library):
            break
        else:
            print('Invalid choice.')
            continue
    editing = library[uinput-1]

    if "Circle" in editing.name:
        editing = Circle(int_input('radius'), 0, 0, editing.name)
    elif "Square" in editing.name:
        editing = Square(int_input('side length'), 0, 0, editing.name)
    elif "Rectangle" in editing.name:
        editing = Rectangle(int_input('side length'), int_input('base length'), 0, 0, editing.name)
    elif "Triangle" in editing.name:
        editing = Triangle(int_input('height'), int_input('base length'), 0, 0, editing.name)

    library[uinput-1] = editing

    return library

def create(library, cir_count, tri_count, squ_count, rec_count):
    while True:
        uinput = input('what shape would you like to make: 1: Circle, 2: Triangle, 3: Square, 4: Rectangle ')
        if uinput == '1':
            library.append(Circle(int_input('radius')))
            cir_count += 1
            break
        elif uinput == '3':
            library.append(Square(int_input('side length')))
            squ_count += 1
            break
        elif uinput == '4':
            library.append(Rectangle(int_input('side length'), int_input('base length')))
            rec_count += 1
            break
        elif uinput == '2':
            library.append(Triangle(int_input('height'), int_input('base length')))
            tri_count += 1
            break
        else:
            print("Invalid input.")
    return library, cir_count, tri_count, squ_count, rec_count
        
        
library = []

library, cir_count, tri_count, squ_count, rec_count = create(library, cir_count, tri_count, squ_count, rec_count)

print(library[0])