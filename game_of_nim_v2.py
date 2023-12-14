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
        self.myTextLabel6 = "wow"
        self.myTextLabel7Text = tk.StringVar()
        self.myTextLabel7 = None
        self.myTextLabel8Text = tk.StringVar()
        self.myTextLabel8 = None
        self.myTextLabel9Text = tk.StringVar()
        self.myTextLabel9 = None
        self.myTextLabel10Text = tk.StringVar()
        self.myTextLabel10 = None

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
        self.root.after(1000, self.clear_label5)

    def create_label6(self, labeltext6=""):
        self.myTextLabel6Text.set(labeltext6)
        self.myTextLabel6 = tk.Label(self.root, textvariable=self.myTextLabel6Text, font=('Verdana', 10), bg='#333333', fg='white')
        self.myTextLabel6.place(relx=0.5, rely=0.3, anchor='center')

    def create_label7(self, labeltext7=""):
        self.myTextLabel7Text.set(labeltext7)
        self.myTextLabel7 = tk.Label(self.root, textvariable=self.myTextLabel7Text, font=('Verdana', 10), bg='#333333', fg='white')
        self.myTextLabel7.place(relx=0.5, rely=0.2, anchor='center')

    def create_label8(self, labeltext8=""):
        self.myTextLabel8Text.set(labeltext8)
        self.myTextLabel8 = tk.Label(self.root, textvariable=self.myTextLabel8Text, font=('Verdana', 10), bg='#333333', fg='white')
        self.myTextLabel8.place(relx=0.5, rely=0.2, anchor='center')

    def create_label10(self, labeltext6=""):
        self.myTextLabel10Text.set(labeltext6)
        self.myTextLabel10 = tk.Label(self.root, textvariable=self.myTextLabel10Text, font=('Verdana', 10), bg='#333333', fg='white')
        self.myTextLabel10.place(relx=0.5, rely=0.4, anchor='center')

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
        self.create_label6("How many balls do you want to remove")
        self.create_textbox2()
        self.create_button2("Submit")

    def button1_handler(self):
        print("Button 1 clicked!")
        txt = self.myTextBox1.get()
        # self.myTextBox1Text.set(txt)  # Store the entered text
        message = "Welcome, {0}, to the Games of Nim version 2.0!".format(txt)
        self.myTextLabel2.destroy()
        self.myTextBox1.destroy()
        self.myButton1.destroy()
        self.create_label3(message)

    def fun_remove_balls(self, remove_value):
        self.number_of_balls -= remove_value
        return self.number_of_balls

    def fun_comp_turn(self):
        remove_value = self.number_of_balls % 5
        self.number_of_balls -= remove_value
        return remove_value

    def create_label9(self, labeltext9=""):
        self.myTextLabel9Text.set(labeltext9)
        self.myTextLabel9 = tk.Label(self.root, textvariable=self.myTextLabel9Text, font=('Verdana', 10), bg='#333333',
                                     fg='red')
        self.myTextLabel9.place(relx=0.5, rely=0.5, anchor='center')

    def clear_label9(self):
        self.myTextLabel9Text.set("")

    def clear_label6(self):
        self.myTextLabel6Text.set("")
        self.create_label9("")

    def clear_label9(self):
        self.myTextLabel9Text.set("")
        self.myTextLabel9 = tk.Label(self.root, textvariable=self.myTextLabel9Text, font=('Verdana', 10), bg='#333333',
                                     fg='white')
        self.myTextLabel9.place(relx=0.5, rely=0.5, anchor='center')

    def hide_submit_button(self):
        self.myButton2.place_forget()

    def show_submit_button(self):
        self.myButton2.place(relx=0.5, rely=0.44, anchor='center')

    def button2_handler(self):
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
            message = f'You removed {txt2}, The computer removed {comp_remove_value} ball(s), There are {self.number_of_balls} ball(s) remaining.'
            self.clear_label6()
            self.create_label7(message)
            self.create_label6("How many balls do you want to remove")
            self.create_textbox2()
            self.show_submit_button()

            if self.number_of_balls == 0:
                comp_message = f'Computer won!'

                self.clear_label6()
                self.create_label8(comp_message)
                self.hide_submit_button()
                self.create_restart_button()


    def restart_game(self):
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
        self.myButton1.destroy()
        self.restart_button = tk.Button(self.root, text="Restart Game", font=('Verdana', 10), command=self.restart_game)
        self.restart_button.place(relx=0.5, rely=0.3, anchor='center')
        # Hide the textbox and the submit button
        self.myTextBox2.place_forget()
        # self.hide_submit_button()

    def create_label7(self, labeltext7=""):
        self.myTextLabel7Text.set(labeltext7)
        self.myTextLabel7 = tk.Label(self.root, textvariable=self.myTextLabel7Text, font=('Verdana', 10), bg='#333333', fg='white')
        self.myTextLabel7.place(relx=0.5, rely=0.2, anchor='center')

    def create_label8(self, labeltext8=""):
        self.myTextLabel8Text.set(labeltext8)
        self.myTextLabel8 = tk.Label(self.root, textvariable=self.myTextLabel8Text, font=('Verdana', 10), bg='#333333', fg='white')
        self.myTextLabel8.place(relx=0.5, rely=0.25, anchor='center')

# "New"
    def create_quit_button(self):
        quit_button = tk.Button(self.root, text="Quit", font=('Verdana', 10), command=self.quit_game)
        quit_button.place(relx=0.5, rely=0.9, anchor='center')

    def quit_game(self):
        self.root.destroy()
def main():

    myGUI = NimII("Games of Nim V2.0")
    myGUI.create_label1("Welcome to the Games of Nim V2.0")
    myGUI.create_quit_button()
    myGUI.root.mainloop()


if __name__ == "__main__":
 main()