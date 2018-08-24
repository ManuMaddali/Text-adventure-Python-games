import random
import math
import sys
import os

def start_game():                           #Started game loop
    name = input("Please enter your name to start the game: ")
    print("Player " + str(name) + " has entered the game!")
    input()
    print("     ***************************")
    print("       *    THE ADVENTURE    *  ")
    print("     ***************************")
    print("              **********")
    print("              ****BY****")
    print("              **********")
    print("     $$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("     $$$$$$$ Manu Maddali $$$$$$$")
    print("     $$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    input()
    print("")
    print("You enter a dark room with door #1 and door #2")
    input()
    print("You don't know what is behind either doors")
    input()
    print("Each door has some form of danger that you have to overcome to reach a speical treasure")
    input()
    print("However... once you go into a door, the only way to come back to the dark room is to lose 50 HP")
    input()
    playerHP = str(100)
    print("Current HP: " + playerHP)
    input()
    print("You will find many weapons and ammunitions throughout the game")
    input()
    print("Now you get to choose one of your starting weapon: 1.Dagger or 2.Pickaxe. Enter 1 or 2)")
    weapon = input()
    if weapon == '1':
        Dagger()
    elif weapon == '2':
        Pickaxe()
    else:
        print("Answer not valid, please try again")
        start_game()
def Dagger():
    input()
    print("You chose the Dagger!")
    input()
    print("The Dagger is swift but lacks in power")
    input()
    door_choose()
def Pickaxe():
    input()
    print("You chose the Pickaxe!")
    input()
    print("The Pickaxe is a powerful weapon, but lacks in speed")
    input()
    door_choose()
def game_restart():        #Player comes back to this point when they die in door1
    restChoice = input("Restart to choose a different door? Yes/No: ")
    if restChoice == "Yes":
        input()
        door_choose()
    elif restChoice == "No":
        input()
        start_game()
    else:
        start_game()

def door_choose():          #Point where players choose thier doors
    print("Which door do you choose: ")


    door = input("> ")

    if door == "1":
        print("You enter door #1")
        input()
        print("You see a mighty dragon")
        input()
        print("Beside you is a Pistol, you pick it up")
        input()
        print("ROARRRRRR!!!")
        input()
        print("The dragon wakes up right as you pick up your pistol")
        input()
        print("You decide to shoot the dragon")
        input()
        print("The dragon is more powerful. ")
        input()
        print("The dragon kills you")
        input()
        door_choose()

    elif door == "2":               #Storyline for door2
        print("You enter door #2")
        input()
        print("You enter a simulation where humans are controlled by machines")
        input()
        print("You see something coming at you at an increadble amount of speed")
        input()
        flight_flight()
def chest_choice():             #Function for whats inside the chest
    choice1 = input("Do you open it? Yes/No")
    if choice1 == "Yes":
        print("You see vending machine for weapons(Strange?)")
        input()
        print("Listed are the weapons and their prices")
        input()
        print("Cash on hand: $10")
        input()
        print("1. Pistol - $5")
        print("2. Shotgun - $15")
        print("3. Machine gun - $30")
        print("4. Grenade Launcher - $60")
        print("5. RPG - $100")
        print("6. Nuke - $400")
    elif choice1 == "No":
        print("The object kills you")
    else:
        print("END")
        start_game()
def flight_flight():        #Function for enemy1
    wht_todo = input("What do you do, Run or Fight: ")
    if wht_todo == "Run":
        print("You run to the nearest shelter, an abandoned and rusty windmill")
        input()
        print("While peeking through the cracks you see a giant, grotesque creature.")
        input()
        print("Something hits your feet...")
        input()
        print("You look down and see a treasure chest")
        chest_choice()



    else:
        print("Done!")

start_game()
