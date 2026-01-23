#AS 2nd Random Password Generator
#Credit for slow_type() function goes to stack overflow user Bill Gross

import sys,time,random

typing_speed = 999 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print('')
slow_type("pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp")

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


def upper():
    pass

def lower():
    pass

def special():
    pass

def length():
    pass
