from distutils.command.config import config
from tkinter import *
import math

#-------------------------------------- CONSTANTS ----------------------------------------#
FONT_NAME = "Courier"
BG_COLOR = "#C4DAD2"
FG_COLOR = "#16423C"
BTN_BG_COLOR = "#E9EFEC"
#-------------------------------------- TIME RESET ----------------------------------------#

#-------------------------------------- TIME MECHANISM ----------------------------------------#
def start_timer():
    count_down(5 * 60)

#-------------------------------------- COUNTDOWN MECHANISM ----------------------------------------#
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)



#-------------------------------------- UI SETUP ----------------------------------------#

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=BG_COLOR)


title_label = Label(text="Timer", fg=FG_COLOR, font=(FONT_NAME, 50, "bold"), bg=BG_COLOR,)
title_label.grid(column=1, row=0)

canvas = Canvas(width=530, height=530, bg=BG_COLOR, highlightthickness=0)
images_clock = PhotoImage(file="pngwing.com.png")
canvas.create_image(265, 265, image=images_clock)
timer_text = canvas.create_text(265, 205, text="00:00", fill="black", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


start_button = Button(text="Start", font=("", 15, "bold"), highlightthickness=5, bg=BG_COLOR, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=("", 15, "bold"), highlightthickness=5, bg=BG_COLOR)
reset_button.grid(column=2, row=2)

check_mark = Label(text="✔", bg=BG_COLOR, fg=FG_COLOR,)
check_mark.grid(column=1, row=2)






window.mainloop()




