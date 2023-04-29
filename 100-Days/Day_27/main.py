from tkinter import *


def button_clicked():
    print("I got clicked")
    new_input = input.get()
    my_label.config(text=new_input)

window = Tk()
window.title("My first GUI program")  # to add title
window.minsize(width=500, height=300)  # to set size
window.config(padx=20, pady=20)

# Label

my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=1, row=1)  # showing label onto the screen


# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=2)

button2 = Button(text="Click Here", command=button_clicked)
button2.grid(column=3, row=1)

# Entry
input = Entry(width=10)
input.grid(column=4, row=3)




window.mainloop()
