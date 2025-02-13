from Character import Character

def narrate(*messages):
    for message in messages:
        input(message)

def look_around(message):
    return message

def fight(enemy_weapon):
    char_weapon = Character.get_weapon
    if char_weapon == None:
        char_weapon = "fists"
       
    fight_choice = input(f"Do you attack with your {char_weapon} or try to block?\n1. Attack\n2. Block\n3. Dodge")
    if fight_choice == "1":
        return "Fight"
    elif fight_choice == "2":
        return "Block"
    elif fight_choice == "3":
        return "Dodge"
    else:
        return "Nothing"