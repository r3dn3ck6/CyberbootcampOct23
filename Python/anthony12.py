#This is just a fun text based adventure game that can be played in side the terminal still updating and expading this to make it more indpeth and more intresting uses random number genreation
#to decide if certain events are effective or not we added some familar charchters to the game to make it more fun and enjoyable
# Setup

import random
yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]
 
# Introduction
name = input("What is your name, adventurer?\n")
print("Greetings, " + name + ". Let us go on a quest!")
print("You find yourself on the edge of a dark forest.")
print("Can you find your way through?\n")
 
# Start of game
response = ""
while response not in yes_no:
    response = input("Would you like to step into the forest?\nyes/no\n")
    if response == "yes":
        print("You head into the forest. You hear crows cawwing in the distance.\n")
    elif response == "no":
        print("You are not ready for this quest. Goodbye, " + name + ".")
        quit()
    else: 
        print("I didn't understand that.\n")
 
# Next part of game
response = ""
while True:
    print("To your left, you see a witch.")
    print("To your right, there is more forest.")
    print("There is a rock wall directly in front of you.")
    print("Behind you is the forest exit.\n")
    response = input("What direction do you move?\nleft/right/forward/backward\n")
    if response == "left":
        print("You encounter a witch in a house made of candy what do you do?")
        fight = input("fight the witch y/n\n")
        if  fight == "y":
            print("10 sided dice rolled to see if you beat witch you need a 5 or higher")
            number = random.randint(1, 10)
            if number >= 5:
                print(f"you have defeated the witch with a roll of {number} and escaped the forest with a friendly cat name binx")
                response = ""
            else: print("You rolled less than 5 the witch and throws you in the oven") 
            quit()
        else: print("you ran away")
        
    elif response == "right":
        print("You head deeper into the forest.  You find a castle in front of you.\n")
        castle = input("You enter the castle do you go left or right?\n")
        if castle == "left":
            print("You fall through a trap door and find a hulk. You find a bow and arrows next to you.")
            troll = input("\nDo you shoot the hulk or try to run.  shoot/run\n")
            if troll == "shoot":
                arrow = random.randint(1, 10)
                print("You try and shoot the hulk with 70% accuracy")
                if arrow <= 7:
                    print("You shoot the hulk and escape the castle")
                    quit()
                else: print("You try and shoot the hulk and miss and then you get hulksmashed.")
            else: print("You try and run from the hulk but he catches you and throws you in the dungeon.")
            quit()
        else:  print("You head to the right and find a staircase and start to asscend you get to the top and find the princess.\n")  
        princess = input("Do you try and save her?y/n\n")
        if princess == "y":
                print("You save the princess and escape the castle")
        else: print("The princess shoots you for being an asshole")
        quit()
    elif response == "forward":
        wall = input("You find a wall you can climb do you climb it?.y/n\n")
        if wall == "y":
            print("You scale the wall and find a dragon")
            dragon = input("Do you charm the dragon or run? c/r\n")
            if dragon == "c":
                print("You charm the dragon and ride it to safety")
                quit()   
            else: print("The dragon is the child of Daenerys Targaryen and she ask you to bend the knee but you believe Tirion should lead the seven kingdoms so she burns you alive")
            quit()
        else: print("You turn back and get lost and find a creature guarding a ring?")
        print("The creatures call the ring my prescious")
        ring = input("Do you take the ring from him?y/n\n")
        if ring == "y":
            print("You take a chance to steal the ring.")
            rings = random.randint(1, 10)
            if rings >= 5:
                print(f"Your rolled a {rings}")
                print("You take your chance to steal the ring and grab it and harness its power to escape")
            else: print(f"You rolled a {rings}.  The creature catches you and throw you into a pit to never been seen again")
        else: print("The creatures is greatful you did not try and steal his prescious and leads you to the exit") 
        
        response = "" 
    elif response == "backward":
            print("A magical door to the forest slams behind you and now you are stuck.")
            cave = input("Do you got to the cave or the tower?\n")
            if cave == "cave":
                print("You find tony stark stuck in cave building a suit and help him escape and you escape also")
            else: print("You find the true boogeyman John Wick and he kills all the creatures of the forest and you become ruler of the forest as he leaves to avenge the death of his dog")
    else:
        print("I didn't understand that.\n")
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
Collapse


















