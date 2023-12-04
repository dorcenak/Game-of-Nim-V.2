import tkinter as tk
import random

class NimII:
    def __init__(self, windowtext):
        self.root = tk.Tk()
        self.root.geometry('800x500')
        self.root.resizable(False, False)
        self.root.title(windowtext)
        self.root.configure(bg='#333333')  # Dark gray background
        self.number_of_balls = random.randint(15, 100)  # Generate a random number of balls to start the game
        self.message_number_of_balls = "Let's start with {0} balls.".format(self.number_of_balls)
        self.balls_remaining = None
        self.balls_removed = None

        self.myButton1 = None
        self.myButton2 = None
        self.myTextBox1 = tk.Entry(self.root)
        self.myTextBox1Text = tk.StringVar()  # Store entered text
        self.myTextBox2 = tk.Entry(self.root)
        self.myTextBox2Text = tk.StringVar()  # Store entered text
        self.myTextLabel1Text = tk.StringVar()
        self.myTextLabel1 = None
        self.myTextLabel2Text = tk.StringVar()
        self.myTextLabel2 = None
        self.myTextLabel3Text = tk.StringVar()
        self.myTextLabel3 = None
        self.myTextLabel4Text = tk.StringVar()
        self.myTextLabel4 = None
        self.myTextLabel5Text = tk.StringVar()
        self.myTextLabel5 = "Let's start with {0} balls.".format(self.number_of_balls)
        self.myTextLabel6Text = tk.StringVar()
        self.myTextLabel6 = None
        self.myTextLabel7Text = tk.StringVar()
        self.myTextLabel7 = None

    def create_label1(self, labeltext=""):
        self.myTextLabel1Text.set(labeltext)
        self.myTextLabel1 = tk.Label(self.root, textvariable=self.myTextLabel1Text, font=('Verdana', 26), bg='#333333', fg='white')
        self.myTextLabel1.place(relx=0.5, rely=0.45, anchor='center')
        self.root.after(2000, self.clear_label1)

    def create_textbox1(self):
        self.myTextBox1.grid(row=3, column=8, sticky=tk.E + tk.W, pady=10)
        self.myTextBox1.place(relx=0.5, rely=0.382, anchor='center')

    def create_textbox2(self):
        self.myTextBox2.grid(row=3, column=8, sticky=tk.E + tk.W, pady=10)
        self.myTextBox2.place(relx=0.5, rely=0.382, anchor='center')

    def create_label2(self, labeltext2=''):
        self.myTextLabel2Text.set(labeltext2)
        self.myTextLabel2 = tk.Label(self.root, textvariable=self.myTextLabel2Text, font=('Verdana', 10), bg='#333333', fg='white')
        self.myTextLabel2.place(relx=0.5, rely=0.34, anchor='center')

    def create_label3(self, labeltext3=''):
        self.myTextLabel3Text.set(labeltext3)
        self.myTextLabel3 = tk.Label(self.root, textvariable=self.myTextLabel3Text, font=('Verdana', 10), bg='#333333', fg='white')
        self.myTextLabel3.place(relx=0.5, rely=0.5, anchor='center')
        self.root.after(1000, self.clear_label3)

    def create_label4(self, labeltext4='There are the rules'):
        self.myTextLabel4Text.set(labeltext4)
        self.myTextLabel4 = tk.Label(self.root, textvariable=self.myTextLabel4Text, font=('Verdana', 10), bg='#333333', fg='white')
        self.myTextLabel4.place(relx=0.5, rely=0.2, anchor='center')
        self.root.after(1000, self.clear_label4)

    def create_label5(self, labeltext5):
        self.myTextLabel5Text.set(labeltext5)
        self.myTextLabel5 = tk.Label(self.root, textvariable=self.myTextLabel5Text, font=('Verdana', 10), bg='#333333', fg='white')
        self.myTextLabel5.place(relx=0.5, rely=0.2, anchor='center')

    def create_label6(self, labeltext6="How many balls do you want to remove"):
        self.myTextLabel6Text.set(labeltext6)
        self.myTextLabel6 = tk.Label(self.root, textvariable=self.myTextLabel6Text, font=('Verdana', 10), bg='#333333', fg='white')
        self.myTextLabel6.place(relx=0.5, rely=0.2, anchor='center')

    def create_label7(self, labeltext7=""):
        self.myTextLabel7Text.set(labeltext7)
        self.myTextLabel7 = tk.Label(self.root, textvariable=self.myTextLabel7Text, font=('Verdana', 10), bg='#333333', fg='white')
        self.myTextLabel7.place(relx=0.5, rely=0.2, anchor='center')

    def create_button1(self, buttontext="", command=None):
        self.myButton1 = tk.Button(self.root, text=buttontext,  font=('Verdana', 10), command=self.button1_handler)
        self.myButton1.place(relx=0.5, rely=0.44, anchor='center')

    def create_button2(self, buttontext2="", command=None):
        self.myButton2 = tk.Button(self.root, text=buttontext2, font=('Verdana', 10), command=self.button2_handler)
        self.myButton2.place(relx=0.5, rely=0.44, anchor='center')

    def clear_label1(self):
        self.myTextLabel1Text.set("")
        self.create_label2("Insert your name:")
        self.create_textbox1()
        self.create_button1("Submit")

    def clear_label3(self):
        self.myTextLabel3Text.set("")
        self.create_label4()

    def clear_label4(self):
        self.myTextLabel4Text.set("")
        self.create_label5(self.message_number_of_balls)

    def clear_label5(self):
        self.myTextLabel5Text.set("")
        self.create_label6()
        self.create_textbox2()

    def button1_handler(self):
        print("Button 1 clicked!")
        txt = self.myTextBox1.get()
        # self.myTextBox1Text.set(txt)  # Store the entered text
        message = "Welcome, {0}, to the Games of Nim version 2.0!".format(txt)
        self.myTextLabel2.destroy()
        self.myTextBox1.destroy()
        self.myButton1.destroy()
        self.create_label3(message)

    def button2_handler(self):
        print("Button 2 clicked!")
        txt2 = self.myTextBox2.get()
        # self.myTextBox1Text.set(txt)  # Store the entered text
        message = "You removed {0}, The computer removed {1} balls, There are {2} balls remaining".format(txt2)
        self.myTextLabel6.destroy()
        self.myTextBox2.destroy()
        self.myButton2.destroy()
        self.create_label7(message)

    #     self.display_message_progressively(message, 0, self.display_final_scene)  # Do not call the callback here
    #
    # def display_message_progressively(self, message, index, callback):
    #     if index < len(message):
    #         current_text = self.myTextLabel3Text.get()
    #         current_text += message[index]
    #         self.myTextLabel3Text.set(current_text)
    #         self.root.after(100, self.display_message_progressively, message, index + 1, callback)
    #     else:
    #         # Adjust the timing based on the length of the message
    #         self.root.after(100 * len(message), callback)
    # #
    # def display_final_scene(self):
    #     user_name = self.myTextBox1Text.get()  # Retrieve stored text
    #     welcome_message = "Welcome, {0}, to the Games of Nim version 2.0!".format(user_name)
    #     self.myTextLabel3Text.set(welcome_message)

    # def fun_remove_balls(self, balls_remaining - None, ):
    #     self.balls_remaining -= self.myTextBox2Text
    #     return self.balls_remaining
    #
    # def fun_comp_turn(self, balls_remaining):
    #     remove_value = balls_remaining % 5
    #     balls_remaining = balls_remaining - remove_value
    #     return remove_value


def main():
    myGUI = NimII("Games of Nim V2.0")
    myGUI.create_label1("Welcome to the Games of Nim V2.0")
    myGUI.root.mainloop()


    # while myGUI.myTextBox2Text < 1 or myGUI.myTextBox2Text > 4:
    #     print("Number must be between 1 and 4.")
    #     myGUI.create_label6()
    #     myGUI.create_textbox2()
    #     myGUI.create_button2()
    # myGUI.number_of_balls = myGUI.fun_remove_balls(myGUI.number_of_balls, myGUI.remove_balls)
    # print(f'You took {remove_balls} ball(s).')
    # print(f'{number_of_balls} ball(s) remaining.')
    #
    # if number_of_balls == 0:
    #     print("You won")
    # else:
    #     remove_value = fun_comp_turn(number_of_balls)
    #     print(f'Computer takes {remove_value} ball(s).')
    #     number_of_balls = fun_remove_balls(number_of_balls, remove_value)
    #     print(f'{number_of_balls} ball(s) remaining.')
    #
    #     if number_of_balls == 0:
    #         print("The computer won")

if __name__ == "__main__":
    main()
