# CSC226 Final Project

❗️Exclamation Marks ❗️indicate action items; you should remove these emoji as you complete/update the items which they accompany. (This means that your final README should have no ❗️in it!)

**Author(s)**: Kichemy & Diego

**Google Doc Link**: https://docs.google.com/document/d/1iyLxrsavHL-QFgBKrcvRiFc25MP0h0UUUf7HaLXz0MA/edit?usp=sharing

---

❗**References**: 
Throughout this project, you have likely used outside resources. Reference all ideas which are not your own, and describe how you integrated the ideas or code into your program. This includes online sources, people who have helped you, and any other resources that are not solely your own contribution. Update as you go.

---

## Milestone 1: Setup, Planning, Design

**Title**: 
  Game of Nim Mark II

**Purpose**: 
  Our project will work in the same manner as the original game of nim but with the change 
of making the code generate a random starting amount of balls.

**Sources**: 
  Our project will be based on homework 6: The Game of Nim.
**CRC Card(s)**:
  
![alt text](image/CRC.png "Image of CRC card as an example. Upload your CRC card(s) in place of this one")

**Branches**: 
1. Branch 1 name: kichemy-branch
2. Branch 2 name: DACC-branch

---

## Milestone 2: Code

No README action items. Keep your issue queue up to date, and focus on your code. 🙃

Your repository should have, at a minimum, two branches; one for each partner, each with their contributions. 
-Diego A. Colorado:
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
---

## Milestone 3: Virtual Check-In

Indicate what percentage of the project you have left to complete and how confident you feel. 

❗️**Completion Percentage**: 0 - 100%

❗️**Confidence**: Describe how confident you feel about completing this project, and why. Then, describe some strategies you can employ to increase the likelihood that you'll be successful in completing this project before the deadline.

❗️Keep your issue queue up to date, and continue to refine your code!

---

## Milestone 4: Final Code, Presentation, Demo

### ❗User Instructions
In a paragraph, explain how to use your program. Assume the user is starting just after they hit the "Run" button in PyCharm. 

### ❗Errors and Constraints
Every program has bugs or features that had to be scrapped for time. 
These bugs should be tracked in the issue queue. You should already have a few items in here from the prior weeks. 
Create a new issue for any undocumented errors and deficiencies that remain in your code. 
Bugs found that aren't acknowledged in the queue will be penalized.

### ❗Reflection
In three to four well-written paragraphs, address the following (at a minimum):
- Why did you select the project that you did?
- How closely did your final project reflect your initial design?
- What did you learn from this process?
- What was the hardest part of the final project?
- What would you do differently next time, knowing what you know now?
