from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("Day_31/data/words_to_learn.csv")
except FileExistsError:
    original_data = pandas.csv("Day_31/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text = current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back)

def is_known():
    to_learn.remove(current_card)
    pandas.DataFrame(to_learn)
    data.to_csv("Day_31/data/words_to_learn.csv", index=False)
    next_card()

# ----------------------UI SETUP--------------------------#
window = Tk()
window.title("FlashCard")
window.config(padx=100, pady=50, bg=BACKGROUND_COLOR)
window.minsize(width=500, height=300)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg = BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="Day_31/images/card_front.png")
card_back = PhotoImage(file="Day_31/images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 260, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong = PhotoImage(file="Day_31/images/wrong.png")
red_button = Button(image=wrong, highlightthickness=0, command=next_card)
red_button.grid(row=1, column=0)

right = PhotoImage(file="Day_31/images/right.png")
green_button = Button(image=right, highlightthickness=0, command=is_known)
green_button.grid(row=1, column=1)


next_card()


window.mainloop()