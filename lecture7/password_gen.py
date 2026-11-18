import tkinter
import random 
from pathlib import Path

from file_reader import read_file

adjectives = read_file(str(Path(__file__).resolve().parent / "adjectives.txt"))
nouns = read_file(str(Path(__file__).resolve().parent / "nouns.txt"))

def generate_password() -> str:
    # draw an adjective
    adjective = random.choice(adjectives)
    # draw a noun
    noun = random.choice(nouns)
    # draw a number between 0 and 100
    number = random.randint(0, 100)
    # draw a special character
    special_char = random.choice("!@#$%^&*()-+")
    # combine and return
    return f"{adjective}{noun}{number}{special_char}"

def generate_pw_command():
    pw = generate_password()
    pw_label.configure(text=f"Generated password:{pw}")

# GUI business
main_window = tkinter.Tk()
main_window.title("Password-Generator")
canvas = tkinter.Canvas(main_window, width=400, height=150)
canvas.grid(row=0, column=0, rowspan=2, columnspan=1)

gen_pw_button = tkinter.Button(main_window, text="Generate new password", command=generate_pw_command)
gen_pw_button.grid(row=0, column=0)

pw_label = tkinter.Label(main_window, text="Generated password:")
pw_label.grid(row=1, column=0)
main_window.mainloop()