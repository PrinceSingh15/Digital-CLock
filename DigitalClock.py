import sys
from tkinter import *
import time

def times():
    current_time = time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(200,times)

root = Tk()
root.geometry("500x250")

frame = Label(root, bg = "#08403C")
frame.place(relx = 0.0, rely =0.0, relheight = 1, relwidth = 1)

clock = Label(root, font = ("times 50 bold"), bg="#E1F00D")
clock.grid(row=2, column=2, pady=25, padx=100)
times()

digi = Label(root, text = "DIGITAL CLOCK", font = ("times 30 bold"), bg = "#E1F00D")
digi.grid(row = 0, column = 2)

display = Label(root, text = "Hour      minutes      seconds", font= ("times 15 bold"), bg = "#E1F00D")
display.grid(row=3, column = 2)

root.mainloop()
