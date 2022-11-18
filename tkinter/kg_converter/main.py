from tkinter import Tk, Entry, Label, Button

window = Tk()
window.title("weight converter")
window.config(padx=20, pady=20)

KG_TO_POUND = 2.20462


def calculate(event=None):
    masukan = user_input.get()
    hasil = f"{int(masukan) * KG_TO_POUND:.2f}"
    result.config(text=hasil)


user_input = Entry(width=15)
user_input.grid(column=2, row=1)
user_input_label = Label(text="kg", font="consolas")
user_input_label.grid(column=3, row=1)

new_label = Label(text="is equal to", font="consolas")
new_label.grid(column=1, row=2)

result = Label(text="0", font="consolas")
result.grid(column=2, row=2)

result_label = Label(text="Pound", font="consolas")
result_label.grid(column=3, row=2)

button = Button(text="Calculate", font="consolas", command=calculate)
button.grid(column=2, row=3)

window.bind("<Return>", func=calculate)
window.mainloop()
