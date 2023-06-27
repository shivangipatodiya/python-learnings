from tkinter import *


def calculate_miles_to_km():
    value = entered_value.get()
    answer = float(value) * 1.609
    output_value.config(text=answer)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

entered_value = Entry(width=10)
entered_value.grid(column=2, row=0)
entered_value.focus()
label_1 = Label(text="Miles")
label_1.grid(column=3, row=0)
label_2 = Label(text="is equal to ")
label_2.grid(column=1, row=1)
label_3 = Label(text="Km ")
label_3.grid(column=3, row=1)
calculate_button = Button(text="Calculate", command=calculate_miles_to_km)
calculate_button.grid(column=2, row=2)
output_value = Label(text="0")
output_value.grid(column=2, row=1)

window.mainloop()
