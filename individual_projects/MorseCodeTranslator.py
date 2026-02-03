#AS 2nd Morse Code Translator

#make function to translate string to morse code
def become_morse(listin, listout, uinput):
    output = []
    for i in list(uinput):
        if i.lower() in listin:
            index = listin.index(i)
            output.append(listout[index])
        else:
            pass
    return ' '.join(output)

#make function to translate morse code to string
def un_morse(listin, listout, uinput):
    output = []
    morse = []
    val = 0
    uinput = uinput.split(' ')
    for i in uinput:
        if i.lower() in listin:
            index = listin.index(i)
            output.append(listout[index])
        else:
            pass
    return ''.join(output)

#make lists for translation
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']

#run main program
print ("Welcome to morse code translator 2026")
while "franklin consumes lightly warmed and crusted slices of a flour based food invented by the mesopotamians":
    uinput = input("Would you like to 1: Encode a message, 2: Decode a message, 3: Leave. ")
    if uinput == '1':
        uinput = input("What is your message? ")
        print(become_morse(alpha, morse, uinput))
    elif uinput == '2':
        uinput = input("What is your message? ")
        print(un_morse(morse, alpha, uinput))
    elif uinput == '3':
        break
    else:
        print("Invalid input.")
        continue
print("Thank you for visiting Mr.Morse's morse code thing.")