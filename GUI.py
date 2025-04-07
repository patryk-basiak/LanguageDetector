import tkinter as tk
import tkinter.constants
from tkinter.constants import BOTTOM, TOP
from Service import analyze
from tkinter import messagebox
class Gui:
    def __init__(self):
        self.clicked = False
        self.root = tk.Tk()
        self.root.title("Language detector")
        self.text = tk.Text(self.root, height=8)
        self.myButton = tk.Button(self.root, text="Detect language", command=self.my_click)
        self.text.pack(padx=10, pady=10, expand=True, fill=tk.BOTH, side=TOP)
        self.myButton.pack(padx=10, pady=10, expand=True, side=BOTTOM)
        self.label = tk.Label(self.root, text="")
        self.label.pack(padx=5, pady=5, side=BOTTOM)
        self.root.mainloop()

    def my_click(self):
        print("Clicked")
        a = analyze(self.text.get("1.0",'end-1c'), data_form="String")
        self.text.delete('1.0', tkinter.END)
        self.label.config(text=f'Result language detected is {a[0]}')

