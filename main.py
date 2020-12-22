from tkinter import *
from pprint import pprint
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
Timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_count():
    global reps
    reps = 0
    window.after_cancel(Timer)     #Timer為windows.after的程式名字
    timer_label.config(text="Timmer")
    canves.itemconfigure(count_text, text="00:00")
    check_mark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_count():
    global reps
    reps += 1
    print(reps)
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:                                   #每8次大休息
        timer_label.config(text="Break", fg=RED)
        time_count(long_break_sec)
    elif reps % 2 == 1:                                 #為1、3、5、7工作
        timer_label.config(text = "Work", fg=GREEN)
        time_count(work_sec)
    elif reps % 2 == 0:                                 #為2、4、6小休息
        timer_label.config(text="Break", fg=PINK)
        time_count(short_break_sec)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def time_count(count):
    count_min = math.floor(count / 60)       # floor取整數無條件捨去
    count_sec = count % 60
    if count_sec < 10:         #讓9、8、7等個位數顯示09、08、07
        count_sec = f"0{count_sec}"
    canves.itemconfigure(count_text, text=f"{count_min}:{count_sec}")

    if count >0:
        global Timer
        count -= 1
        Timer = window.after(1000, time_count, count) #每過1000毫秒達行 time_count方程式，方程式變數為count
    else:
        start_count()
        global reps
        mark = ""
        mark_action = math.floor(reps/2)  #用除法後必定是float為確保只取得整數部分
        for _ in range(mark_action):
            mark += "✔"
            check_mark.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)


canves = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)   # highlightthickness為了解決圖片白邊問題
tomato_img = PhotoImage(file="tomato.png")  # tkinter的圖片必須用這程式取圖片資料
canves.create_image(100, 110, image=tomato_img)
count_text = canves.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canves.grid(column=1, row=1)



timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
timer_label.grid(column=1, row=0)

# pprint(dict(timer_label)) # 查屬性很方便的東西

start_button = Button(text="Start", command=start_count)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_count)
reset_button.grid(column=2, row=2)

check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()