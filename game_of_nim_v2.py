######################################################################
# Author(s): Kichemy & Diego
# Username(s): dorcenak & coloradod
#
# Assignment: Final Project
#
# Purpose: Our project use the tkinter library to implement a GUI window that
# features and updated version of the Game of NIm. The only difference in the algorithm is that the number of balls
# that is generated at the beginning of the game is random.
######################################################################
# Acknowledgements: hw06: The Game of Nim by Kichemy & Jaela for the algorithm we use in our game
#                   t12-guis-events-team-6 to know how to implement the GUI window
#                   TA Steevenson for bugs such as creating the first new buttons and keep the loop going as
#                   we have balls in the game.
#
#
####################################################################################


import tkinter as tk
import random


class NimII:
    """
    Prompt the user to enter their name and provide instructions on how to play the game.
    """

    def __init__(self, windowtext, balls_remaining=None, balls_removed=None, myButton1=None, myButton2=None,
                 myTextLabel1=None, myTextLabel2=None, myTextLabel3=None, myTextLabel4=None, myTextLabel5=None,
                 myTextLabel6=None, myTextLabel7=None, myTextLabel8=None, myTextLabel9=None, myTextLabel10=None):
        """
        A constructor for the NimII class

        :param windowtext: The title of the GUI window.
        :param balls_remaining: The number of balls remaining in the game.
        :param balls_removed: The amount of balls the user/computer decides to remove each time they play.
        :param myButton1: The first button where the user clicks to perform a specific action.
        :param myButton2: The second button where the user clicks to perform another specific action.
        :param myTextLabel1-10: Text for each specific prompt displayed on the GUI window.
        """
        self.root = tk.Tk()
        self.root.geometry('800x500')
        self.root.resizable(False, False)
        self.root.title(windowtext)
        self.root.configure(bg='#333333')  # Dark gray background
        self.number_of_balls = random.randint(15, 100) if balls_remaining is None else balls_remaining
        self.message_number_of_balls = "Let's start with {0} balls.".format(self.number_of_balls)
        self.balls_remaining = balls_remaining
        self.balls_removed = balls_removed

        self.myButton1 = myButton1
        self.myButton2 = myButton2

        self.myTextBox1 = tk.Entry(self.root)
        self.myTextBox1Text = tk.StringVar()  # Store entered text
        self.myTextBox2 = tk.Entry(self.root)
        self.myTextBox2Text = tk.StringVar()  # Store entered text

        self.myTextLabel1Text = tk.StringVar()
        self.myTextLabel1 = myTextLabel1
        self.myTextLabel2Text = tk.StringVar()
        self.myTextLabel2 = myTextLabel2
        self.myTextLabel3Text = tk.StringVar()
        self.myTextLabel3 = myTextLabel3
        self.myTextLabel4Text = tk.StringVar()
        self.myTextLabel4 = myTextLabel4
        self.myTextLabel5Text = tk.StringVar()
        self.myTextLabel5 = myTextLabel5
        self.myTextLabel6Text = tk.StringVar()
        self.myTextLabel6 = myTextLabel6
        self.myTextLabel7Text = tk.StringVar()
        self.myTextLabel7 = myTextLabel7
        self.myTextLabel8Text = tk.StringVar()
        self.myTextLabel8 = myTextLabel8
        self.myTextLabel9Text = tk.StringVar()
        self.myTextLabel9 = myTextLabel9
        self.myTextLabel10Text = tk.StringVar()
        self.myTextLabel10 = myTextLabel10

    def create_textbox1(self):
        """
        Display a textbox for the user to enter information.

        :param row: Row index in the grid where the textbox should be placed.
        :param column: Column index in the grid where the textbox should be placed.
        :param sticky: A string that determines where the widget would be placed in its grid cell.
                       It is a combination of N, S, E, W, NE, NW, SE, SW, or their combinations (e.g., 'tk.E + tk.W').
        :param pady: Vertical padding around the textbox.
        :param relx: Relative x-coordinate for placing the textbox using place geometry manager.
        :param rely: Relative y-coordinate for placing the textbox using place geometry manager.
        :param anchor: Determines a point in the textbox to be placed at the relative coordinates (e.g., 'center').
        """
        # Grid the textbox at specified row, column, and sticky configuration
        self.myTextBox1.grid(row=3, column=8, sticky=tk.E + tk.W, pady=10)

        # Place the textbox at specified relative coordinates and anchor point
        self.myTextBox1.place(relx=0.5, rely=0.382, anchor='center')

    def create_textbox2(self):
        """
        Display a second textbox for the user to enter information.

        :param row: Row index in the grid where the textbox should be placed.
        :param column: Column index in the grid where the textbox should be placed.
        :param sticky: A string that determines where the widget would be placed in its grid cell.
                       It is a combination of N, S, E, W, NE, NW, SE, SW, or their combinations (e.g., 'tk.E + tk.W').
        :param pady: Vertical padding around the textbox.
        :param relx: Relative x-coordinate for placing the textbox using place geometry manager.
        :param rely: Relative y-coordinate for placing the textbox using place geometry manager.
        :param anchor: Determines a point in the textbox to be placed at the relative coordinates (e.g., 'center').

        :return: None
        """
        # Grid the textbox at specified row, column, and sticky configuration
        self.myTextBox2.grid(row=3, column=8, sticky=tk.E + tk.W, pady=10)

        # Place the textbox at specified relative coordinates and anchor point
        self.myTextBox2.place(relx=0.5, rely=0.382, anchor='center')

    def create_label1(self, labeltext=""):
        """
        Create and display a label with specified text.

        :param labeltext: The text to be displayed in the label.
        :return: None
        """
        # Set the text for the label
        self.myTextLabel1Text.set(labeltext)

        # Create a label with specified properties
        self.myTextLabel1 = tk.Label(self.root, textvariable=self.myTextLabel1Text, font=('Verdana', 26), bg='#333333',
                                     fg='#00FFFF')

        # Place the label at specified relative coordinates and anchor point
        self.myTextLabel1.place(relx=0.5, rely=0.45, anchor='center')

        # Schedule the label to be cleared after 2000 milliseconds (2 seconds)
        self.root.after(2000, self.clear_label1)

    def create_label2(self, labeltext2=''):
        """
        Create and display a second label with specified text.

        :param labeltext2: The text to be displayed in the label.
        :return: None
        """
        self.myTextLabel2Text.set(labeltext2)
        self.myTextLabel2 = tk.Label(self.root, textvariable=self.myTextLabel2Text, font=('Verdana', 10), bg='#333333',
                                     fg='#FFFFE0')
        self.myTextLabel2.place(relx=0.5, rely=0.34, anchor='center')

    def create_label3(self, labeltext3=''):
        """
        Create and display a third label with specified text.

        :param labeltext3: The text to be displayed in the label.
        :return: None
        """
        self.myTextLabel3Text.set(labeltext3)
        self.myTextLabel3 = tk.Label(self.root, textvariable=self.myTextLabel3Text, font=('Verdana', 18), bg='#333333',
                                     fg='#00FFFF')
        self.myTextLabel3.place(relx=0.5, rely=0.45, anchor='center')
        self.root.after(3000, self.clear_label3)

    def create_label4(self, label_texts=['RULES:', '1.You have to play first.',
                                         '2.You cannot remove a number of balls that is neither lower than 1 nor higher than 5.',
                                         '3.You will lose if the computer removes the last number of balls.']):
        """
        Create and display a fourth label with specified multiline text.

        :param label_texts: List of strings representing multiline text for the label.
        :return: None
        """
        label_text = '\n'.join(label_texts)
        self.myTextLabel4Text.set(label_text)
        self.myTextLabel4 = tk.Label(self.root, textvariable=self.myTextLabel4Text, font=('Verdana', 13), bg='#333333',
                                     fg='#1E90FF')
        self.myTextLabel4.place(relx=0.5, rely=0.3, anchor='center')
        self.root.after(10000, self.clear_label4)

    def create_label5(self, labeltext5=""):
        """
        Create and display a fifth label with specified text.

        :param labeltext5: The text to be displayed in the label.
        :return: None
        """
        self.myTextLabel5Text.set(labeltext5)
        self.myTextLabel5 = tk.Label(self.root, textvariable=self.myTextLabel5Text, font=('Verdana', 10), bg='#333333',
                                     fg='white')
        self.myTextLabel5.place(relx=0.5, rely=0.2, anchor='center')
        self.root.after(1000, self.clear_label5)

    def create_label6(self, labeltext6=""):
        """
        Create and display a sixth label with specified text.

        :param labeltext6: The text to be displayed in the label.
        :return: None
        """
        self.myTextLabel6Text.set(labeltext6)
        self.myTextLabel6 = tk.Label(self.root, textvariable=self.myTextLabel6Text, font=('Verdana', 10), bg='#333333',
                                     fg='#FFFFE0')
        self.myTextLabel6.place(relx=0.5, rely=0.3, anchor='center')

    def create_label7(self, labeltext7=""):
        """
        Create and display a seventh label with specified text.

        :param labeltext7: The text to be displayed in the label.
        :return: None
        """
        self.myTextLabel7Text.set(labeltext7)
        self.myTextLabel7 = tk.Label(self.root, textvariable=self.myTextLabel7Text, font=('Verdana', 10), bg='#333333',
                                     fg='#008000')
        self.myTextLabel7.place(relx=0.5, rely=0.2, anchor='center')

    def create_label8(self, labeltext8=""):
        """
        Create and display an eighth label with specified text.

        :param labeltext8: The text to be displayed in the label.
        :return: None
        """
        self.myTextLabel8Text.set(labeltext8)
        self.myTextLabel8 = tk.Label(self.root, textvariable=self.myTextLabel8Text, font=('Verdana', 10), bg='#333333',
                                     fg='white')
        self.myTextLabel8.place(relx=0.5, rely=0.2, anchor='center')

    def create_label9(self, labeltext9=""):
        """
        Create and display a ninth label with specified text.

        :param labeltext9: The text to be displayed in the label.
        :return: None
        """
        self.myTextLabel9Text.set(labeltext9)
        self.myTextLabel9 = tk.Label(self.root, textvariable=self.myTextLabel9Text, font=('Verdana', 10), bg='#333333',
                                     fg='red')
        self.myTextLabel9.place(relx=0.5, rely=0.5, anchor='center')

    def create_label10(self, labeltext6=""):
        """
        Create and display a tenth label with specified text.

        :param labeltext6: The text to be displayed in the label.
        :return: None
        """
        self.myTextLabel10Text.set(labeltext6)
        self.myTextLabel10 = tk.Label(self.root, textvariable=self.myTextLabel10Text, font=('Verdana', 10),
                                      bg='#333333', fg='white')
        self.myTextLabel10.place(relx=0.5, rely=0.4, anchor='center')

    def create_button1(self, buttontext="", command=None):
        """
        Create and display the first button with specified text and command.

        :param buttontext: The text to be displayed on the button.
        :param command: The function to be executed when the button is clicked.
        :return: None
        """
        self.myButton1 = tk.Button(self.root, text=buttontext, font=('Verdana', 10), command=self.button1_handler,
                                   bg="#228B22")
        self.myButton1.place(relx=0.5, rely=0.44, anchor='center')

    def create_button2(self, buttontext2="", command=None):
        """
        Create and display the second button with specified text and command.

        :param buttontext2: The text to be displayed on the button.
        :param command: The function to be executed when the button is clicked.
        :return: None
        """
        self.myButton2 = tk.Button(self.root, text=buttontext2, font=('Verdana', 10), command=self.button2_handler,
                                   bg="#228B22")
        self.myButton2.place(relx=0.5, rely=0.44, anchor='center')

    def clear_label1(self):
        """
        Clear the first label and initiate the creation of the second label, a textbox, and the first button.

        :return: None
        """
        self.myTextLabel1Text.set("")
        self.create_label2("Insert your name:")
        self.create_textbox1()
        self.create_button1("Submit")

    def clear_label3(self):
        """
        Clear the third label and initiate the creation of the fourth label.

        :return: None
        """
        self.myTextLabel3Text.set("")
        self.create_label4()

    def clear_label4(self):
        """
        Clear the fourth label and initiate the creation of the fifth label.

        :return: None
        """
        self.myTextLabel4Text.set("")
        self.create_label5(self.message_number_of_balls)

    def clear_label5(self):
        """
        Clear the fifth label and initiate the creation of the sixth label, a textbox, and the second button.

        :return: None
        """
        self.myTextLabel5Text.set("")
        self.create_label6("How many balls do you want to remove?")
        self.create_textbox2()
        self.create_button2("Submit")

    def button1_handler(self):
        """
        Handler for the first button click event.

        :return: None
        """
        print("Button 1 clicked!")
        txt = self.myTextBox1.get()
        # self.myTextBox1Text.set(txt)  # Store the entered text
        message = "Welcome, {0}, to the Game of Nim version 2.0!".format(txt)
        self.myTextLabel2.destroy()
        self.myTextBox1.destroy()
        self.myButton1.destroy()
        self.create_label3(message)

    def fun_remove_balls(self, remove_value):
        """
        Function to update the number of balls by subtracting the specified value.

        :param remove_value: The value to be subtracted from the current number of balls.
        :return: Updated number of balls.
        """
        self.number_of_balls -= remove_value
        return self.number_of_balls

    def fun_comp_turn(self):
        """
        Function to determine the computer's turn by calculating the value to remove.

        :return: The value to be removed by the computer.
        """
        remove_value = self.number_of_balls % 5
        self.number_of_balls -= remove_value
        return remove_value

    def clear_label9(self):
        """
        Clear the ninth label.

        :return: None
        """
        self.myTextLabel9Text.set("")

    def clear_label6(self):
        """
        Clear the sixth label and initiate the creation of the ninth label.

        :return: None
        """
        self.myTextLabel6Text.set("")
        self.create_label9("")

    def create_label8(self, labeltext8=""):
        """
        Create and display an eighth label with specified text.

        :param labeltext8: The text to be displayed in the label.
        :return: None
        """
        self.myTextLabel8Text.set(labeltext8)
        self.myTextLabel8 = tk.Label(self.root, textvariable=self.myTextLabel8Text, font=('Verdana', 10), bg='#333333',
                                     fg='white')
        self.myTextLabel8.place(relx=0.5, rely=0.25, anchor='center')

    def clear_label9(self):
        """
        Clear the ninth label and initiate the creation of the ninth label.

        :return: None
        """
        self.myTextLabel9Text.set("")
        self.myTextLabel9 = tk.Label(self.root, textvariable=self.myTextLabel9Text, font=('Verdana', 10), bg='#333333',
                                     fg='white')
        self.myTextLabel9.place(relx=0.5, rely=0.5, anchor='center')

    def hide_submit_button(self):
        """
        Hide the submit button.

        :return: None
        """
        self.myButton2.place_forget()

    def show_submit_button(self):
        """
        Show the submit button.

        :return: None
        """
        self.myButton2.place(relx=0.5, rely=0.44, anchor='center')

    def button2_handler(self):
        """
        Handler for the second button click event.

        :return: None
        """
        print("Button 2 clicked!")
        txt2 = self.myTextBox2.get()

        if not txt2.isdigit() or not (1 <= int(txt2) <= 4):
            error_message = "Please enter a number between 1 and 4."
            self.create_label9(error_message)
            return

        txt2 = int(txt2)

        # Reset the textbox
        self.myTextBox2.delete(0, tk.END)

        # Perform the game logic
        self.number_of_balls = self.fun_remove_balls(txt2)

        if self.number_of_balls == 0:
            message = f'You removed {txt2} ball(s). You won!'
            self.create_label7(message)
            self.create_label8("Press 'Restart Game' to play again.")
            self.hide_submit_button()
            self.create_restart_button()
        else:
            comp_remove_value = self.fun_comp_turn()
            message = f'You removed {txt2} ball(s), The computer removed {comp_remove_value} ball(s), There are {self.number_of_balls} ball(s) remaining.'
            self.clear_label6()
            self.create_label7(message)
            self.create_label6("How many balls do you want to remove?")
            self.create_textbox2()
            self.show_submit_button()

            if self.number_of_balls == 0:
                comp_message = f'Sorry, the computer won!'

                self.clear_label6()
                self.create_label8(comp_message)
                self.hide_submit_button()
                self.create_restart_button()

    def restart_game(self):
        """
        Restart the game.

        :return: None
        """
        # Reset game variables and labels
        self.number_of_balls = random.randint(15, 100)
        self.message_number_of_balls = "Let's start with {0} balls.".format(self.number_of_balls)
        self.myTextLabel7Text.set("")
        self.myTextLabel8Text.set("")
        self.clear_label9()  # Clear the error message
        self.create_label5(self.message_number_of_balls)

        # Show the textbox and the submit button
        self.myTextBox2.place(relx=0.5, rely=0.382, anchor='center')

        # Hide the "Restart Game" button
        self.restart_button.place_forget()

    def create_restart_button(self):
        """
        Create and display the "Restart Game" button.

        :return: None
        """
        self.myButton1.destroy()
        self.restart_button = tk.Button(self.root, text="Restart Game", font=('Verdana', 10), command=self.restart_game,
                                        bg="#228B22")
        self.restart_button.place(relx=0.5, rely=0.3, anchor='center')
        # Hide the textbox and the submit button
        self.myTextBox2.place_forget()
        # self.hide_submit_button()

    def create_label7(self, labeltext7=""):
        """
        Create and display the seventh label with specified text.

        :param labeltext7: The text to be displayed in the label.
        :return: None
        """
        self.myTextLabel7Text.set(labeltext7)
        self.myTextLabel7 = tk.Label(self.root, textvariable=self.myTextLabel7Text, font=('Verdana', 10), bg='#333333',
                                     fg='white')
        self.myTextLabel7.place(relx=0.5, rely=0.2, anchor='center')

    def create_quit_button(self):
        """
        Create and display the quit button.

        :return: None
        """
        quit_button = tk.Button(self.root, text="Quit", font=('Verdana', 10), command=self.quit_game, bg="#CE2029")
        quit_button.place(relx=0.5, rely=0.9, anchor='center')

    def quit_game(self):
        """
        Quit the game.

        :return: None
        """
        self.root.destroy()

def main():
    """
    Main function to initiate the GUI.

    :return: None
    """
    myGUI = NimII("Games of Nim V2.0")
    myGUI.create_label1("Games of Nim V2.0")
    myGUI.create_quit_button()
    myGUI.root.mainloop()


if __name__ == "__main__":
    main()
