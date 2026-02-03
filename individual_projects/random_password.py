#AS 2nd Random Password Generator
#Credit for slow_type() function goes to stack overflow user Bill Gross

import sys,time,random,string

typing_speed = 999 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print('')

def num():
    while True:
        need_num = input("Do you need numbers in your password? Y/N: ")
        if need_num.lower() == "y":
            return True
            break
        elif need_num.lower() == "n":
            return False
            break
        else:
            print("Invalid choice.")
            continue

usage = {'uppercase letters': 'n', 'lowercase letters': 'n', 'numbers': 'n', 'special characters': 'n', 'length': 0}

def what_to_use(usage):
    for i in usage:
        if i == 'length':
            while 78:
                uinput = input("How long must the password be? ")
                if uinput.isdigit():
                    uinput = int(uinput)
                    usage[i] = uinput
                    break
                else:
                    print("Invalid input.")
                    continue
        else:
            while 238:
                uinput = input(f"Does the password require {i}? Y/N ")
                if uinput.lower() == 'y' or uinput.lower() == 'n':
                    usage[i] = uinput.lower()
                    break
                else:
                    print("Invalid input.")
                    continue
    return usage



def generator(usage):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    special = ['_', '@', '$', '#']
    for y in range(1, 5):
        password = []
        if usage['uppercase letters'] == 'y':
            password.append(random.choice(upper))
        else:
            pass
        if usage['lowercase letters'] == 'y':
            password.append(random.choice(lower))
        else:
            pass
        if usage['special characters'] == 'y':
            password.append(random.choice(special))
        else:
            pass
        if usage['numbers'] == 'y':
            password.append(str(random.randint(0, 9)))
        else:
            pass
        for x in range(usage['length']):
            while 689:
                choice = random.randint(1, 4)
                if choice == 1:
                    if usage['uppercase letters'] == 'y':
                        password.append(random.choice(upper))
                        break
                    else:
                        continue
                if choice == 2:
                    if usage['lowercase letters'] == 'y':
                        password.append(random.choice(lower))
                    else:
                        continue
                if choice == 3:
                    if usage['special characters'] == 'y':
                        password.append(random.choice(special))
                        break
                    else:
                        continue
                if choice == 4:
                    if usage['numbers'] == 'y':
                        password.append(str(random.randint(0, 9)))
                        break
                    else:
                        continue
        final = ''.join(password)
        slow_type(f"Option {y}: {final}")
        print('')

def run():
    usage = {'uppercase letters': 'n', 'lowercase letters': 'n', 'numbers': 'n', 'special characters': 'n', 'length': 0}
    while 1098:
        uinput = input("Would you like to 1: generate a password, or 2: leave? ")
        if uinput == '1':
            usage = what_to_use(usage)
            generator(usage)
            continue
        elif uinput == '2':
            break
        else:
            print("Invalid choice.")
            continue

print("Welcome!")
run()
print("Goodbye!")