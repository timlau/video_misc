import tkinter as tk

# from tkinter import ttk

from ui import FONT_BOLD, FONT_NORMAL


class GridEntryLine:
    def __init__(self, parent, text, row: int, default="") -> None:
        self.label = tk.Label(parent, text=text, anchor=tk.W, font=FONT_BOLD, width=40)
        self.label.grid(row=row, column=1, columnspan=6, sticky=tk.W, padx=5)
        self.entry = tk.Entry(parent, font=FONT_NORMAL, text=default, width=80)
        self.entry.grid(
            row=row + 1, column=1, columnspan=6, sticky=tk.W, padx=20, pady=10
        )


class GridEntry:
    def __init__(self, parent: tk.Widget, text: str, default, row: int, col: int):
        data = tk.StringVar()
        data.set(default)
        label = tk.Label(parent, text=text, font=FONT_NORMAL, width=10)
        label.grid(row=row, column=col, padx=5, sticky=tk.W)
        self.entry = tk.Entry(parent, textvariable=data, width=6)
        self.entry.grid(row=row, column=col + 1, pady=10, sticky=tk.W)
