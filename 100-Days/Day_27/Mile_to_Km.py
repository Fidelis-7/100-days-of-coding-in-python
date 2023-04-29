from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
# window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

is_equal_label = Label(text="is equal to", font=("Arial", 14, "bold"))
is_equal_label.grid(column=0, row=1)

Miles_label = Label(text="Miles", font=("Arial", 14, "bold"))
Miles_label.grid(column=2, row=0)

Kilometer_result_label = Label(text=0)
Kilometer_result_label.grid(column=1, row=1)

Kilometer_label = Label(text="Km", font=("Arial", 14, "bold"))
Kilometer_label.grid(column=2, row=1)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    Kilometer_result_label.config(text=f"{km}")


calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)


window.mainloop()