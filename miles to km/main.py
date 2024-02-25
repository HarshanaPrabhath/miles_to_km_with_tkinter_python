from tkinter import *

window = Tk()
window.title("Miles to km converter")
window.config(padx=50, pady=50)


def calculate():
    miles = float(input_mile.get())
    km = miles * 1.60934
    km_result.config(text=f"{km}")


input_mile = Entry(width=10)
input_mile.grid(row=0, column=2)

mile_label = Label(text="Miles")
mile_label.grid(row=0, column=3)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(row=1, column=1)

km_result = Label(text="0")
km_result.grid(row=1, column=2)

km_label = Label(text="km")
km_label.grid(row=1, column=3)

calculate_button = Button(text="calculate", command=calculate)
calculate_button.grid(row=2, column=2)

window.mainloop()

