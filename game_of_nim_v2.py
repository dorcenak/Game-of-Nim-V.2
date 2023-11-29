import random
def display_remains(strtV1):
    print("Total balls remaining:", strtV1)

def player_move(strtV1):
    while True:
        try:
            tkp1 = input("Awesome! How many balls from 1 to 4 would you like to take away?")
            tkp1 = int(tkp1)
            if 1 <= tkp1 <= 4 and tkp1 <= strtV1:
                return tkp1
            else:
                print("I'm sorry. Only a value between 1 and 4 can be entered.")
        except ValueError:
            print("I'm sorry. please put in a different value.")

def computer_turn(strtV1):
    comp_subtract = random.randint(1, min(4, strtV1))
    print("The computer took away", comp_subtract, "balls.")
    return comp_subtract

def ball_input():
    usr_name = input("Hello. What is your name?")
    print("Hi "+usr_name+"!")
    q1 = input("Would you like to play a game?")
    if q1 == 'yes':
        comp_subtract = random.randint(15, min(99, strtV1))
        strtV1 = int(input("Awesome! How many balls do you want to start off with? The amount has to be at or higher than 15 though."))

        if strtV1 >= 15:
            player_turn = True
            while strtV1 > 0:
                display_remains(strtV1)

                if player_turn:
                    subtracted = player_move(strtV1)
                else:
                    subtracted = computer_turn(strtV1)

                strtV1 -= subtracted
                player_turn = not player_turn
            display_remains(strtV1)
            if player_turn:
                print("Congratulations! You win!")
            else:
                print("The computer won. Get destroyed.")
        else:
            print("I'm sorry. That number cannot be entered")
    else:
        print("Okay. See you next time then!")

ball_input()
