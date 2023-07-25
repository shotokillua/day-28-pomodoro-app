from tkinter import *
import math
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
tick_tock = ""

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps
    reps = 0
    window.after_cancel(tick_tock)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        timer_label.config(text="Long Break", fg=RED)
        countdown(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        timer_label.config(text="Short Break", fg=PINK)
        countdown(SHORT_BREAK_MIN * 60)
    else:
        timer_label.config(text="Work", fg=GREEN)
        countdown(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def countdown(time):
    global tick_tock
    count_min = math.floor(time / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = time % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if time > 0:
        tick_tock = window.after(1000, countdown, time - 1)
    else:
        start_timer()
        checks = ""
        work_sessions = math.floor(reps/2)
        for num in range(work_sessions):
            checks += "✓"
        check_label.config(text=checks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
# highlightthickness=0 eliminates the border around a label or button or widget


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 40, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

check_label = Label(font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)


window.mainloop()
