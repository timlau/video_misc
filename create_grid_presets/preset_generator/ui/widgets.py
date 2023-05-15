import tkinter as tk

# from tkinter import ttk

from ui import FONT_BOLD, FONT_NORMAL


class PackEntry:
    def __init__(self, parent, text, default="") -> None:
        self.label = tk.Label(parent, text=text, anchor=tk.W, font=FONT_BOLD)
        self.label.pack(padx=10, pady=5, fill=tk.X)
        self.entry = tk.Entry(parent, font=FONT_NORMAL, text=default)
        self.entry.pack(padx=10, pady=10, fill=tk.X)


class GridEntry:
    def __init__(self, parent: tk.Widget, text: str, default, row: int, col: int):
        data = tk.StringVar()
        data.set(default)
        label = tk.Label(parent, text=text, font=FONT_NORMAL)
        label.grid(row=row, column=col, padx=5)
        self.entry = tk.Entry(parent, textvariable=data)
        self.entry.grid(row=row, column=col + 1, pady=10)
