import tkinter

window = tkinter.Tk()
window.title("halo")
window.minsize(width=800, height=800)


label = tkinter.Label(text="halo")
label.grid(column=1, row=1)


button = tkinter.Button(fg="red", bg="blue", text="new button")
button.grid(column=2, row=2)

new_button = tkinter.Button(fg="blue", text="new button")
new_button.grid(column=3, row=1)


new_input = tkinter.Entry(width=10)
new_input.grid(column=4, row=3)
window.mainloop()
