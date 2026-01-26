#--------------------

# Random Password Generator Program
# By Armaan Ahmed

#--------------------
#import
from tkinter import *
import random


#variables
root = Tk()

small_alpha = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
big_alpha = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
numbers = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
symbols = ("!", "@", "#", "$", "%", "&", "*", "_", "-")

password = ""
passwords = []

#Password Conditions
has_small_alpha = BooleanVar()
has_big_alpha = BooleanVar()
has_number = BooleanVar()
has_symbol = BooleanVar()

#Functions
def center_window(window): #centers the tkinter window in the center of the screen
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width+40}x{height+40}+{x-40}+{y-40}")

def generate(): #generating password command

    password_copied_message.config(text="", bg="#0A0F3D")
    global password, password_background
    password = ""
    password_background = "#0A0F3D"
    if (has_small_alpha.get() or has_big_alpha.get() or has_number.get() or has_symbol.get()) == False:
        password_background="#0A0F3D"
    else:
        password_background="#1E1B51"
        while (len(password) < password_length_scale.get()):
            x = random.randint(1, 4)
            if (x == 1) and (has_small_alpha.get() == True):
                y = random.randint(0, 25)
                password += small_alpha[y]
            if (x == 2) and (has_big_alpha.get() == True):
                y = random.randint(0, 25)
                password += big_alpha[y]
            if (x == 3) and (has_number.get() == True): 
                y = random.randint(0, 9)
                password += numbers[y]
            if (x == 4) and (has_symbol.get() == True):
                y = random.randint(0, 8)
                password += symbols[y]

    info_label.config(text=password, bg=password_background)
    if len(password) == 0:
        pass
    else:
        passwords.append(password)

def copy_password(): #copy the generated password
    global text
    text = password
    root.clipboard_clear()
    root.clipboard_append(text)
    if len(password) != 0:
        password_copied_message.config(text="Copied", bg="#1E1B51")
    else:
        pass

def terminate(): #close the program
    root.destroy()
    if len(passwords) != 0:
        print("Generated Passwords: ")
        for i in range(len(passwords)):
            print(passwords[i-1])
    else:
        pass

#tkinter elements
info_label = Label(root, text=password, bg="#0A0F3D", fg="#00CED1")
password_length_label = Label(root, text="Choose Password Length", bg="#0A0F3D", fg="#00CED1")
generate_button = Button(root, text="Generate Password", command=generate, bg="#2A235D" ,fg="#5C8BC0")
copy_password_button = Button(root, text="Copy", command=copy_password, bg="#2A235D",fg="#5C8BC0")
terminate_button = Button(root, text="Terminate", command=terminate, bg="#2A235D",fg="#5C8BC0")
password_conditions_label = Label(root, text="Password Conditions",bg="#0A0F3D", fg="#00CED1")
password_copied_message = Label(root, text="",bg="#0A0F3D", fg="#00CED1")

has_small_alpha_check = Checkbutton(root, text="Small Alphabets", variable=has_small_alpha, onvalue=1, offvalue=0, bg="#0A0F3D",fg="#5C8BC0", borderwidth=5)
has_big_alpha_check = Checkbutton(root, text="Big Alphabets", variable=has_big_alpha, onvalue=1, offvalue=0, bg="#0A0F3D",fg="#5C8BC0", borderwidth=5)
has_number_check = Checkbutton(root, text="Numbers", variable=has_number, onvalue=1, offvalue=0, bg="#0A0F3D",fg="#5C8BC0", border=5)
has_symbols_check = Checkbutton(root, text="Symbols", variable=has_symbol, onvalue=1, offvalue=0, bg="#0A0F3D",fg="#5C8BC0", border=5)
password_length_scale = Scale(root, from_=3, to=20, orient=HORIZONTAL, bg="#2A235D",fg="#5C8BC0", troughcolor="#1E1B51")

#places the tkinter elements in the tkinter window
password_conditions_label.grid(row=0, column=0)
has_small_alpha_check.grid(row=1, column=0, sticky=W)
has_big_alpha_check.grid(row=2, column=0, sticky=W) 
has_number_check.grid(row=3, column=0, sticky=W)
has_symbols_check.grid(row=4, column=0, sticky=W)
password_length_scale.grid(row=0, column=1)
password_length_label.grid(row=1, column=1)
generate_button.grid(row=2, column=1)
info_label.grid(row=3, column=1)
password_copied_message.grid(row=4, column=1)   
copy_password_button.grid(row=3, column=2)
terminate_button.grid(row=5, column=1)

#makes it so that everytime you run the program the root window opens
center_window(root)
root.configure(background="#0A0F3D")
root.title("Random Password Generator") 
root.resizable(False, False) #disables resizing
root.mainloop()
