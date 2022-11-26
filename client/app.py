import tkinter as tk
from tkinter import *
import requests
from tkinter import filedialog, Text
import os

root = tk.Tk()
root.geometry("1200x900")


def exit_program():
    root.destroy()


def get_employees():
    pass


canvas = tk.Canvas(root, height=900, width=1200, bg="#f2e8cf", relief="groove")
canvas.pack(fill=BOTH, expand=True)

button_see_employees = tk.Button(canvas, text="See Employees", padx=10, pady=5, bg="#bc4749",
                                 command=get_employees())
button_see_employees.pack()

root.mainloop()
