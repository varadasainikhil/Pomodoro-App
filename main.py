import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer
    global reps
    reps = 0
    window.after_cancel(timer)
    title.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")


# ----------------config------------ TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title.config(text="BREAK", fg=PINK)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title.config(text="BREAK", fg=RED)
    else:
        count_down(WORK_MIN * 60)
        title.config(text="WORK", fg=GREEN)
        check_marks.config(text="✔")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title("Pomodoro App")

title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title.grid(row=0, column=1)

canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
photo_image = PhotoImage(file="tomato.png")
tomato_image = canvas.create_image(103, 112, image=photo_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


def count_down(count):
    global reps
    if count > 0:
        count_seconds = count % 60
        count_minutes = math.floor(count / 60)
        if count_seconds < 10:
            count_seconds = f"0{count_seconds}"
        canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        mark = ""
        start_timer()
        if reps % 2 == 0:
            mark += "✔"
            check_marks.config(text=mark)


start_button = Button(text="Start", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"), command=start_timer)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", fg=RED, bg=YELLOW, font=(FONT_NAME, 15, "bold"), command=reset_timer)
reset_button.grid(row=2, column=2)

check_marks = Label(fg=GREEN, font=(FONT_NAME, 15, "bold"), bg=YELLOW)
check_marks.grid(row=3, column=1)
window.mainloop()
