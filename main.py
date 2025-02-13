from Character import Character
import game_functions as gf

# Initialize an instance of Character named Player.
player = Character(100, None)

# Run the game until won even if the player fails.
while True:
# get the player's name and start the game
    name = input("'Hello there. What is your name?'\n")
    if name == "Rory":
        print("'Nope. You are done.'")
        break
    else:
# shows that the game runs on false choices
# There is a specific path to victory but the game has choices
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

# First choice to look around or wait.
    choice = input("What would you like to do? \n1. Wait for something to happen\n2. Look around \n")

# Wait and do nothing
    if choice == "1":
        gf.narrate("You wait for some time. Nothing happens.",
                "Still waiting.",
                "Still waiting. .",
                "Still waiting. . .")

# Look around the room
    elif choice == "2":
        gf.narrate(gf.look_around("You look around and see a door and a cot."))
        choice = input("Would you like to lay on the cot?\n1. Eww no. Who knows what fluids are on there.\n2. May as well, I'm pretty tired.\n")
# Shows the player a choice can make a difference
        if choice == "1":
            gf.narrate("Good call. You think you see some blood on there.")
# Shows the player there is a health mechanic
        elif choice == "2":
            gf.narrate("It isn't comfortable. In fact, you feel less rested than before.")
            player.lose_health(5)

    gf.narrate("You think about where you came from and how you got here.",
               "You realize you don't remember how you got here.",
               "Eventually, you faintly hear the sound of metal scraping concrete from the other side of the wall.")
    inves = input("Do you investigate? (Y/N) ").lower()

# Approach the door and investigate
# do or do not grab the bat
    if inves == "y":
        gf.narrate("You stand and approach the door.",
                    "As you slowly push the door open,",
                    "the light in the hallway causes you to squint your eyes.",
                    "However, you notice a bat leaning on the wall inside the hallway.")
        bat = input("Take the bat? (Y/N) ").lower()
# grab the bat
        if bat == "y":
            gf.narrate("You take the bat.")
            player.grab_weapon("bat")
            player.add_inventory("bat")
# do not grab the bat
        elif bat == "n":
            gf.narrate("Probably a good idea, violence is never the answer.")

# do not investigate
    elif inves =="n":
        gf.narrate("Good, it is probably something scary.")

    # creature doesn't see you yet
    if inves == "y":
        gf.narrate("The source of the noise becomes apparent.",
                   "Through the door at the end of the hallway steps a creature with three limbs dragging a pipe.",
                   "The creature seems to not have noticed you yet.")
        proceed = input("How will you proceed? ")

# if you don't investigate what to do?  
    elif inves == "n":
        choice = input("What will you do instead?\n1. Look for some sort of indication of where you are.\n2. Nothing.\n")
    # try to find out where you are
        if choice == "1":
            gf.narrate("You look around the small room you are in.",
                       "Other than the bed you woke up on, there doesn't seem to be anything of interest.",
                       "The noise outside the room seems to be getting closer to the door.")
    # don't search  
        elif choice == "2":
            gf.narrate("You sit and wait as the noise outside is getting closer.")
            choice = input("Now what?\n1. Get ready to defend yourself.\n2. Nothing. Accept your fate.\n")
        # prepare yourself or don't, your choice
            if choice == "1":
                gf.narrate("You take a fighting stance as a horrendous creature with three limbs eases the door open.",
                           "You lock eyes with the creature.",
                           "It charges you.")
                print(gf.fight("pipe"))
            elif choice == "2":
                gf.narrate("You stand there. Doing nothing.",
                           "The noise from outside is right outside the door now.")
                choice = input("Still nothing?\n1. NO! DO SOMETHING!\n2. Yep.\n")
            # Try to protect yourself last second.
                if choice == "1":
                    gf.narrate("The monster charges.",
                               "You raise your fists to attempt to block the pipe.")
                    player.lose_health(8)
                    gf.narrate("Blocking the pipe with your fists still hurts, but a lot less.",
                               "The monster swings again and misses, hitting the wall with the pipe.",
                               "The force of the pipe hitting the wall causes the monster to drop it.")
                    choice = input("Will you pick up the pipe? (Y/N)\n").lower()
                    if choice == "y":
                        player.grab_weapon("pipe")
                    elif choice == "n":
                        gf.narrate("What a waste of a good pipe.",
                                   "Oh well, hopefully the monster doesn't pick it back up.",
                                   "It does.")
            # Don't do anything.
                elif choice == "2":
                    gf.narrate("Through the door steps a creature with three arms carrying a pipe.",
                               "You stay still, letting the creature attack you.",
                               "You have nothing to defend yourself with and are not ready.",
                               "Blood splatters the walls as you are beaten to death by a steel pipe.")