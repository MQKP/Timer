import time
import sys
import tkinter as tk
from tkinter import messagebox, TOP
from tkinter.ttk import Button

def countdown(t, window, next_fn=None):
    if t >= 0:
        min, sec = divmod(t, 60)
        mins.set(f"{min:02}")
        seconds.set(f"{sec:02}")

        timeFormat = "{:02d}:{:02d}".format(min, sec)
        label.config(text=timeFormat)
        root.update_idletasks()

        root.after(1000, countdown, t - 1, window, next_fn)
    else:
        if next_fn:
            next_fn()
        else:
            messagebox.showinfo("Completed!", "Study Session Done")

def startStudy(h, window):
    def study_block():
        nonlocal h
        messagebox.showinfo("Chill Time Over", "Get to Studying")
        countdown(3000, window, break_block)

    def break_block():
        nonlocal h
        messagebox.showinfo("Study Break Ended", "Take a Chill Pill")
        h -= 1
        if h > 0:
            countdown(600, window, study_block)
        else:
            countdown(600, window, None)

    study_block()

def center_window(window, width, height):
	screen_width = window.winfo_screenwidth()
	screen_height = window.winfo_screenheight()
	x = (screen_width // 2) - (width // 2)
	y = (screen_height // 2) - (height // 2)
	window.geometry(f'{width}x{height}+{x}+{y}')
	

root = tk.Tk()
root.config(bg = "lightblue")
root.title("Timer")
APP_WIDTH, APP_HEIGHT = 1000, 1000

mins = tk.StringVar()
seconds = tk.StringVar()

mins.set("00")
seconds.set("00")

center_window(root, APP_WIDTH, APP_HEIGHT)

btn = tk.Button(root, text = "Start", command = lambda: startStudy(3, root), width = 10, height = 5)
btn.pack(side = TOP, pady=100)

label = tk.Label(root, text="00:00", font=("Arial", 100), bg="#FFFFFF", fg="black")
label.pack(fill="both", expand=True, pady = 200)

root.mainloop()

