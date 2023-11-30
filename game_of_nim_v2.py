import random
import tkinter as tk
from tkinter import ttk

class NimII:
    """
    A class that will create the window and allow the application to make certain actions
    """
    def __init__(self, windowtext):
        """
         The initializer creates a window to contain the widgets

        :param windowtext: The text at the top of the window title
         """
        self.root = tk.Tk()  # Create the root window where all widgets go
        self.root.minsize(width=800, height=400)  # Sets the window's minimum size
        self.root.maxsize(width=800, height=400)  # Sets the window's maximum size
        self.root.title(windowtext)  # Sets root window title

        self.myButton1 = None

        self.myTextBox1 = tk.Entry(self.root)
        self.myTextLabel1Text = tk.StringVar()  # Makes a Tkinter string variable
        self.myTextLabel1 = None
        self.myCombobox = None

    def create_label1(self, labeltext=""):
        """
        Creates a label on the window and sets the label to labeltext

        :param labeltext: The text on the label
        :return: None
        """

        self.myTextLabel1Text.set(labeltext)  # Sets the Tkinter string variable
        self.myTextLabel1 = tk.Label(self.root, textvariable=self.myTextLabel1Text)
        self.myTextLabel1.grid(row=2, column=8, sticky=tk.E + tk.W, pady=10)

    def create_textbox1(self):
        """
        Creates a textbox into which the user can type

        :return: None
        """

        self.myTextBox1.grid(row=3, column=8, sticky=tk.E + tk.W, pady=10)

    def create_label2(self):
        pass

    def create_textbox2(self):
        pass


def main():
    """
    Creates GUI and uses button, textbox and label GUI widgets

    :return: None
    """

    myGUI = NimII("Games of Nim V2.0")  # Create a new NimII object
    myGUI.create_label1("What is your name?")  # Calls the create button method to create a button
    myGUI.create_textbox1()  # Calls the create textbox method for capturing user input

    myGUI.root.mainloop()  # Needed to start the event loop


if __name__ == "__main__":
 main()
