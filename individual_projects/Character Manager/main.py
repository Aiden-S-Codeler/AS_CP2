#VY 2nd Menu

#Import all functions
from helper import u_input, choice_input
from character_search import search
from user_inputs import input_inventory
from character_create import character_create, Character, Stats
from skill_management import level_up, skill_allocation, skill_reset
from dice import rolling

example = Character("Example", 1, Stats(1, 1, 1, 1), "Orc", 'Mage')

#create example character and character index
example_learned_skills = set()
character_index = [example]
#main menu function
def main_menu():
    #get character function
    def get_character():
        #check if there is a character. If so, search characters. Else, tell them to make a character
        if not character_index:
            print("You must make a character first!")
            character_create(character_index)
        character = search(character_index)
        return character_index[1]
    #loop forever
    while True:
        #get user choice on what to do
        print("\nYou can: \n1. Create a Character \n2. Level up a Character \n3. View a Character \n4. Roll some dice\n5. Exit the Program(This will wipe all data!)")
        user_choice = choice_input(['1','2','3','4','5'],"Type the number that corresponds with the action that you want to perform: ")
        print("")
        match user_choice:
            #character creation
            case "1":
                character_create(character_index)
            
            #character editing
            case "2":
                character = get_character() #get character choice
                character = level_up(character)

            #character viewing
            case "3":
                character = search(character_index)
                print(character)
            
            #dice rolling
            case "4":
                rolling()
            
            #exiting
            case '5':
                break

            #error handling
            case _:
                print("That isn't an option, please try again.")
        
        #clear screen
        input('Press ENTER to continue > ')
        print("\033c", end="")

#run main function
print("This is an RPG Character Manager.")
main_menu()
print("Thank you for using the Character Manager.")