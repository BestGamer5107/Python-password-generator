from tkinter import *
from tkinter import messagebox
import random


alphabet_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
number_chars = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbol_chars = ["@", "$", "#", "!"]
current = []

def Generating():
    try:
        Length = int(length.get())
        
        
        password1 = ""
        
        if Inc_letters.get() == True:
            current.extend(alphabet_chars)
        if Inc_numbers.get() == True:
            current.extend(number_chars)
        if Inc_symbols.get() == True:
            current.extend(symbol_chars)
        
        for i in range(Length):
            password1 += random.choice(current)
        
        
        password2 = StringVar()
        password2.set(password1)
        
        Password.config(textvariable=password2)
        
        current.clear()
        password2 = None
    except ValueError:
        messagebox.showerror(title="ValueError",
                            message="Error: The length of the password must only be a number and not empty")
    except IndexError:
        messagebox.showerror(title="IndexError",
                            message="Error: No characters chosen for the password")


window = Tk()
window.title("Password generator")
window.geometry("425x250")
window.config(bg="Black")
window.resizable(False, False)

Frame1 = Frame(window, bg="Black")
Frame1.pack(pady=10, padx=10, side=TOP)

Frame2 = Frame(window, bg="Black")
Frame2.pack(pady=10, padx=10, side=BOTTOM)

length = Entry(Frame1, font=5)
length.pack(pady=5, padx=5, side=LEFT)

Inc_letters = BooleanVar()
Include_letters = Checkbutton(Frame1, text="Include Letters  ", font=5, variable=Inc_letters, onvalue=True, offvalue=False)
Include_letters.pack(pady=2.5, padx=1, side=TOP)

Inc_numbers = BooleanVar()
Include_numbers = Checkbutton(Frame1, text="Include Numbers", font=5, variable=Inc_numbers, onvalue=True, offvalue=False)
Include_numbers.pack(pady=2.5, padx=1)

Inc_symbols = BooleanVar()
Include_symbols = Checkbutton(Frame1, text="Include Symbols", font=5, variable=Inc_symbols, onvalue=True, offvalue=False)
Include_symbols.pack(pady=2.5, padx=1, side=BOTTOM)

Generate = Button(Frame2, text="Generate", command=Generating, font=10)
Generate.pack(pady=5, padx=5, side=RIGHT)

Password = Entry(Frame2, font=20, state="readonly")
Password.pack(pady=5, padx=5, side=LEFT)

window.mainloop()