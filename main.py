from tkinter import *


def conversion_calculation():
    mi = float(user_input.get())
    km = round(mi * 1.609344, 2)
    converted_num.config(text=km)


window = Tk()
window.title("Conversion Calculator")
window.minsize(width=150, height=150)
window.config(padx=20, pady=20)

miles = Label(text="Miles", font=("Roboto", 12))
miles.grid(column=2, row=0)
miles.config(padx=5,pady=5)

kilometers = Label(text="Km", font=("Roboto", 12))
kilometers.grid(column=2, row=1)
kilometers.config(padx=5,pady=5)

equal_to = Label(text="is equal to", font=("Roboto", 12))
equal_to.grid(column=0, row=1)
equal_to.config(padx=5,pady=5)

converted_num = Label(text=0, font=("Roboto", 12))
converted_num.grid(column=1, row=1)
converted_num.config(padx=5,pady=5)

user_input = Entry(width=10)
user_input.grid(column=1, row=0)


button = Button(text="Convert", command=conversion_calculation)
button.grid(column=1, row=2)
button.config(padx=5,pady=5)

window.mainloop()
