from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Consolas"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
check = ""
reps = 0
timer = None


def start_timer():
    global reps, check
    reps += 1
    work_sec = WORK_MIN * 1
    short_break_sec = SHORT_BREAK_MIN * 1
    long_break_sec = LONG_BREAK_MIN * 1
    if reps % 8 == 0:
        title_label.config(text="take a long break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        check += "✓"
        title_label.config(text="break", fg=PINK)
        check_label.config(text=check)
        count_down(short_break_sec)
    else:
        title_label.config(text="PODO TIMER")
        count_down(work_sec)


def resetTimer():
    global reps, check
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="PODO TIMER")
    reps = 0
    check = ""
    check_label.config(text=check)


def count_down(count):
    min = count // 60
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)


window = Tk()
window.title("Pomodoro Timer")
window.config(padx=50, pady=50, bg=YELLOW)

title_label = Label(text="PODO TIMER", font=(FONT_NAME, 36, "bold"), bg=YELLOW, fg=GREEN)
title_label.grid(column=2, row=1)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0.2)
photo = PhotoImage(file="tkinter/podomoro_timer/tomato.png")
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 26, "bold"))
canvas.grid(column=2, row=2)

start_button = Button(text="start", command=start_timer, font=(FONT_NAME, 12, "bold"))
start_button.grid(column=1, row=3)

check_label = Label(text="", bg=YELLOW, fg=GREEN)
check_label.grid(column=2, row=4)

reset_button = Button(text="Reset", font=(FONT_NAME, 12, "bold"), command=resetTimer)
reset_button.grid(column=3, row=3)


if __name__ == "__main__":
    window.mainloop()
