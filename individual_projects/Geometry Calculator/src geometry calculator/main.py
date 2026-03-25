#AS 2nd geometry calculator

from geofunction import Square, Rectangle, Circle, Triangle, input_check, int_input, compare, view, edit, create

cir_count = 1
tri_count = 1
squ_count = 1
rec_count = 1

library = []

print("Welcome!")
while True:
    uinput = input("Would you like to 1: create a shape, 2: compare shapes, 3: view all shapes, 4: edit a shape,  or 5: leave? ")
    if uinput == '1':
        create(library, cir_count, tri_count, squ_count, rec_count)
    elif uinput == '2':
        print("Please create 2 shapes first")
    elif uinput == '3':
        view(library)
    elif uinput == '4':
        edit(library)
    elif uinput == '5':
        break
    else:
        continue
print('Goodbye.')