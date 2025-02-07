from Character import Character
import game_functions as gf

# Initialize an instance of Character named Player.
player = Character(100, None)

# Run the game until won even if the player fails.
while True:
    name = input("'Hello there. What is your name?'\n")
    if name == "Rory":
        print("'Nope. You are done.'")
        break
    else:
        game = input(f"'Well, {name}, would you like to play a game?' (Y/N) ").lower()
        if game == "y":
            gf.narrate("Good. Let us play.",
                "Here",
                "we",
                "go")          
        elif game == "n":
            gf.narrate("Oh. But it'll be fun.",
                "Here",
                "we",
                "go") 


    gf.narrate("You open your eyes to see a small room. It is just bright enough to make out some of the features in the room.")
    choice = input("What would you like to do? \n1. Wait for something to happen\n2. Look around \n")

    if choice == "1":
        gf.narrate("You wait for some time. Nothing happens.",
                "Still waiting.",
                "Still waiting. .",
                "Still waiting. . .")

    elif choice == "2":
        gf.narrate(gf.look_around("You look around and see a door and a cot."))
        choice = input("Would you like to lay on the cot?\n1. Eww no. Who knows what fluids are on there.\n2. May as well, I'm pretty tired.\n")
        if choice == "1":
            gf.narrate("Good call. You think you see some blood on there.")
        elif choice == "2":
            gf.narrate("It isn't comfortable. In fact, you feel less rested than before.")
            player.lose_health(5)
            gf.narrate(f"You lose some health: Health {player.get_health()}")

    gf.narrate("You stop and think about where you came from and how you got here.",
               "You realize you don't remember how you got here.",
               "Eventually, you faintly hear the sound of metal scraping concrete from the other side of the wall.")
    inves = input("Do you investigate? (Y/N) ").lower()

    if inves == "y":
        gf.narrate("You stand and approach the door.",
                    "As you slowly push the door open,",
                    "the light in the hallway causes you to squint your eyes.",
                    "However, you notice a bat leaning on the wall inside the hallway.")
        bat = input("Take the bat? (Y/N) ").lower()
        if bat == "y":
            gf.narrate("You take the bat.")
            player.grab_weapon("bat")
            player.add_inventory("bat")
        elif bat == "n":
            gf.narrate("Probably a good idea, violence is never the answer.")

    elif inves =="n":
        gf.narrate("Good, it is probably something scary.")

    if inves == "y":
        gf.narrate("The source of the noise becomes apparent.",
                   "Through the door at the end of the hallway steps a creature dragging a hunk of wood.",
                   "The creature seems to not have noticed you yet.")
        
    elif inves == "n":
        choice = input("What will you do instead?\n1. Look for some sort of indication of where you are.\n2. Nothing.")
        
        if choice == "1":
            gf.narrate("You look around the small room you are in.",
                       "Other than the bed you woke up on, there doesn't seem to be anything of interest.",
                       "The noise outside the room seems to be getting closer to the door.")
        
        elif choice == "2":
            gf.narrate("You sit and wait as the noise outside is getting closer.")
            choice = input("Now what?\n1. Get ready to defend yourself.\n2. Nothing. Accept your fate.")
            
            if choice == "1":
                gf.narrate("You take a fighting stance as a horrendous creature with 3 limbs eases the door open.",
                           "You lock eyes with the creature.",
                           "It charges you.")
            elif choice == "2":
                gf.narrate("You stand there. Doing nothing.",
                           "The noise from outside is right outside the door now.")
                choice = input("Still nothing?\n1. NO! DO SOMETHING!\n2. Yep.")