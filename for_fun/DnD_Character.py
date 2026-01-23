# AS dnd random gen

# Stats

import random
stat_1 = [int(random.randint(1, 6)), int(random.randint(1, 6)), int(random.randint(1, 6)), int(random.randint(1, 6))]
stat_1.remove(min(stat_1))
stat_1 = sum(stat_1)
stat_2 = [int(random.randint(1, 6)), int(random.randint(1, 6)), int(random.randint(1, 6)), int(random.randint(1, 6))]
stat_2.remove(min(stat_2))
stat_2 = sum(stat_2)
stat_3 = [int(random.randint(1, 6)), int(random.randint(1, 6)), int(random.randint(1, 6)), int(random.randint(1, 6))]
stat_3.remove(min(stat_3))
stat_3 = sum(stat_3)
stat_4 = [int(random.randint(1, 6)), int(random.randint(1, 6)), int(random.randint(1, 6)), int(random.randint(1, 6))]
stat_4.remove(min(stat_4))
stat_4 = sum(stat_4)
stat_5 = [int(random.randint(1, 6)), int(random.randint(1, 6)), int(random.randint(1, 6)), int(random.randint(1, 6))]
stat_5.remove(min(stat_5))
stat_5 = sum(stat_5)
stat_6 = [int(random.randint(1, 6)), int(random.randint(1, 6)), int(random.randint(1, 6)), int(random.randint(1, 6))]
stat_6.remove(min(stat_6))
stat_6 = sum(stat_6)
print(f"Your stats are: {stat_1}, {stat_2}, {stat_3}, {stat_4}, {stat_5}, {stat_6}")

# Class

class_list = ["Artificer", "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorceror", "Warlock", "Wizard"]
rand_class = int(random.randint(0, 12))
class_chosen = class_list[rand_class]
print(f"Your class is: {class_chosen}")

# Race

race_list = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half Elf", "Halfling", "Half Orc", "Human", "Variant Human", "Teifling", "Aarakocra", "Aasimar", "Air Genasi", "Bug Bear", "Centaur", "Changeling", "Deep Gnome", "Duergar", "Earth Genasi", "Eladrin", "Fairy", "Firbolg", "Fire Genasi", "Githyanki", "Githzerai", "Goblin", "Goliath", "Harengon", "Hobgoblin", "Kenku", "Kobold", "Lizardfolk", "Minotaur", "Orc", "Satyr", "Sea Elf", "Shadar Kai", "Shifter", "Tabaxi", "Tortle", "Triton", "Water Genasi", "Yuan-Ti"]
rand_race = int(random.randint(0, 41))
if rand_race == 0:
    dragonborn_list = ["Red", "Blue", "Black", "White", "Green", "Copper", "Gold", "Brass", "Silver", "Bronze", "Amethyst", "Crystal", "Emerald", "Sapphire", "Topaz"]
    rand_dragonborn = int(random.randint(0, 14))
    race_chosen = dragonborn_list[rand_dragonborn] + " Dragonborn"
else:
    race_chosen = race_list[rand_race]
print(f"Your race is: {race_chosen}")

# where stats go
stat_list = [stat_1, stat_2, stat_3, stat_4, stat_5, stat_6]
stren = 0
dex = 0
con = 0
intel = 0
wis = 0
char = 0
while stren == 0:
    what_stren = input("Which of your stats do you want to be your strength? ")
    if what_stren.isdigit():
        what_stren = int(what_stren)
    else:
        print("Setting strength to 5 for trolling.")
        stren = 5
    if what_stren in stat_list:
        stren = what_stren
        stat_list.remove(what_stren)
    else:
        print("Setting strength to 5 for trolling.")
        stren = 5
print(f"remaining stats are: {stat_list}")
while dex == 0:
    what_dex = input("Which of your stats do you want to be your dexterity? ")
    if what_dex.isdigit():
        what_dex = int(what_dex)
    else:
        print("Setting dexterity to 5 for trolling.")
        dex = 5
    if what_dex in stat_list:
        dex = what_dex
        stat_list.remove(what_dex)
    else:
        print("Setting dexterity to 5 for trolling.")
        dex = 5
print(f"remaining stats are: {stat_list}")
while con == 0:
    what_con = input("Which of your stats do you want to be your constitution? ")
    if what_con.isdigit():
        what_con = int(what_con)
    else:
        print("Setting constitution to 5 for trolling.")
        con = 5
    if what_con in stat_list:
        con = what_con
        stat_list.remove(what_con)
    else:
        print("Setting constitution to 5 for trolling.")
        con = 5
print(f"remaining stats are: {stat_list}")
while intel == 0:
    what_intel = input("Which of your stats do you want to be your inteligence? ")
    if what_intel.isdigit():
        what_intel = int(what_intel)
    else:
        print("Setting inteligence to 5 for trolling.")
        intel = 5
    if what_intel in stat_list:
        intel = what_intel
        stat_list.remove(what_intel)
    else:
        print("Setting inteligence to 5 for trolling.")
        intel = 5
print(f"remaining stats are: {stat_list}")
while wis == 0:
    what_wis = input("Which of your stats do you want to be your wisdom? ")
    if what_wis.isdigit():
        what_wis = int(what_wis)
    else:
        print("Setting wisdom to 5 for trolling.")
        wis = 5
    if what_wis in stat_list:
        wis = what_wis
        stat_list.remove(what_wis)
    else:
        print("Setting wisdom to 5 for trolling.")
        wis = 5
print(f"remaining stats are: {stat_list}")
while char == 0:
    what_char = input("Which of your stats do you want to be your charisma? ")
    if what_char.isdigit():
        what_char = int(what_char)
    else:
        print("Setting charisma to 5 for trolling.")
        char = 5
    if what_char in stat_list:
        char = what_char
        stat_list.remove(what_char)
    else:
        print("Setting charisma to 5 for trolling.")
        char = 5
print(f"Recap:\nYour class is: {class_chosen}\nYour race is: {race_chosen}")
print(f"Your stats are: strength: {stren}, dexterity: {dex}, constitution: {con}, inteligence: {intel}, wisdom: {wis}, dexterity: {dex}")

# Health
lvl = int(input("What is your starting level? "))
health = 0
d12_hlist = ["Barbarian"]
d10_hlist = ["Fighter", "Pladin", "Ranger"]
d8_hlist = ["Artificer", "Bard", "Cleric", "Druid", "Monk", "Rogue", "Warlock"]
d6_hlist = ["Sorceror", "Wizard"]
if class_chosen in d12_hlist:
    health = 12
    for i in range(lvl - 1):
        health = health + random.randint(1, 12)
elif class_chosen in d10_hlist:
    health = 10
    for i in range(lvl - 1):
        health = health + random.randint(1, 10)
elif class_chosen in d8_hlist:
    health = 8
    for i in range(lvl - 1):
        health = health + random.randint(1, 8)
elif class_chosen in d6_hlist:
    health = 6
    for i in range(lvl - 1):
        health = health + random.randint(1, 6)
else:
    pass
print(f"Your total health at your level is {health}")

# Background

background_list = ["Acolyte", "Charlatan", "Criminal/Spy", "Entertainer", "Folk Hero", "Gladiator", "Guild Artisan", "Hermit", "Knight", "Noble", "Outlander", "Pirate", "Sage", "Sailor", "Soldier", "Urchin"]
rand_background = int(random.randint(0, 15))
background_chosen = background_list[rand_background]
print(f"Your background is: {background_chosen}")
rand_personality = random.randint(1, 8)
rand_ideal = random.randint(1, 6)
rand_bond = random.randint(1, 6)
rand_flaw = random.randint(1, 6)
print(f"Your first rolls for background information are: Personality Trait: {rand_personality}, Ideal: {rand_ideal}, Bond: {rand_bond}, Flaw: {rand_flaw}")
rand_personality2 = random.randint(1, 8)
rand_ideal2 = random.randint(1, 6)
rand_bond2 = random.randint(1, 6)
rand_flaw2 = random.randint(1, 6)
while rand_personality2 == rand_personality:
    rand_personality2 = random.randint(1, 8)
while rand_ideal2 == rand_ideal:
    rand_ideal2 = random.randint(1, 6)
while rand_bond2 == rand_bond:
    rand_bond2 = random.randint(1, 6)
while rand_flaw2 == rand_flaw:
    rand_flaw2 = random.randint(1, 6)
print(f"Your second rolls for background information are: Personality Trait: {rand_personality2}, Ideal: {rand_ideal2}, Bond: {rand_bond2}, Flaw: {rand_flaw2}")