# Your challenge wahttonight is to write a basic adventure game using some of the  
#code provide below and using if/elif statments

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
        print("Your mama is a nice lady. You are not ready for this quest. Goodbye, Go Home,  Get a gun! Shoot Yourself- Goodbye 4 ever!, " + name + ".")
        quit()
    else:

# Next part of game
response = ""

# Use if else statment from here to take you on a journey and have fun with it
print("As you venture deeper into the forest, you come across a fork in the path.")

response = ""
while response not in directions:
    response = input("Do you want to go left, right, forward, or backward?\n")
    if response == "left":
        print("You follow the left path and discover an ancient, overgrown temple.")
        print("There's an inscription that reads, 'Only the worthy shallare pass.'")
        response = input("Do you want to enter the temple or continue exploring the forest?\n")
        if response == "enter":
            print("Congratulations, " + name + "! You have proven yourself worthy and found a hidden treasure.")
            print("You win the game! Thanks for playing.")
            quit()
        else:
            print("You continue exploring the forest.")
    elif response == "right":
        print("You take the right path and encounter a mischievous group of fairies.")
        print("They offer you a magical key. What do you want to do?")
        response = input("Take the key or decline?\n")
        if response == "take":
            print("The fairies giggle with joy. The key might be useful later on.")
        else:
            print("The fairies playfully tease you as you continue on your journey.")
    elif response == "forward":
        print("You march forward and find a serene lake with a mysterious glow.")
        print("A wise old turtle surfaces and offers you guidance.")
        print("He tells you to 'follow the moonlight' to reach your destination.")
    elif response == "backward":
        print("You decide to go back. As you turn around, you notice a shadowy figure watching you.")
        print("It disappears into the shadows. What will you do?")
        response = input("Ignore it or investigate?\n")
        if response == "ignore":
            print("You continue on your way, but can't shake the feeling of being watched.")
        else:
            print("You cautiously investigate but find nothing. The forest seems quiet again.")
    else:
        print("I didn't understand that. Please choose left, right, forward, or backward.\n")

print("You continue your adventure. Good luck, " + name + "!")

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
















