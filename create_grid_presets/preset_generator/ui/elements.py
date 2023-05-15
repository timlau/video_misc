import tkinter as tk

from tkinter import ttk
from pathlib import Path

from ui import FONT_BOLD, VideoMode, Grid
from ui.widgets import GridEntry, GridEntryLine


class VideoModeUI:
    def __init__(self, parent, row) -> None:
        label = tk.Label(parent, text="Video Mode", font=FONT_BOLD, anchor=tk.W)
        label.grid(row=row, column=1, columnspan=6, pady=5, padx=5, sticky=tk.W)
        self.width = GridEntry(parent, "Width", default="1920", row=row + 1, col=1)
        self.height = GridEntry(parent, "Height", default="1080", row=row + 1, col=3)
        self.fps = GridEntry(parent, "FPS", default="30", row=row + 1, col=5)

    def read_values(self) -> VideoMode:
        width = int(self.width.entry.get())
        height = int(self.height.entry.get())
        fps = int(self.fps.entry.get())
        return VideoMode(height=height, width=width, fps=fps)


class GridSizeUI:
    def __init__(self, parent, row) -> None:
        label = tk.Label(parent, text="Grid_Size", font=FONT_BOLD)
        label.grid(row=row, column=1, columnspan=6, pady=5, padx=5, sticky=tk.W)
        self.rows = GridEntry(parent, "Rows", default="3", row=row + 1, col=1)
        self.columns = GridEntry(parent, "Columns", default="3", row=row + 1, col=3)
        self.padding = GridEntry(parent, "Padding", default="16", row=row + 1, col=5)

    def read_values(self):
        rows = int(self.rows.entry.get())
        columns = int(self.columns.entry.get())
        padding = int(self.padding.entry.get())
        return Grid(rows=rows, columns=columns, padding=padding)


class SlideUI:
    def __init__(self, parent, row) -> None:
        label = tk.Label(parent, text="Slide", font=FONT_BOLD)
        label.grid(row=row, column=1, pady=5, padx=5)
        self.size = GridEntry(parent, "Size", default="2", row=row + 1, col=1)
        self.duration = GridEntry(parent, "Duration", default="5", row=row + 1, col=3)

    def read_values(self):
        size = int(self.size.entry.get())
        duration = int(self.duration.entry.get())
        return size, duration


class OutputUI:
    def __init__(self, parent, row) -> None:
        self.output = GridEntryLine(parent, "Output directory", row=row, default=".")

    def read_values(self) -> Path:
        return Path(self.output.entry.get()).resolve()


class Selector:
    def __init__(self, parent: tk.Widget, generators: dict, callback: callable):
        self._callback = callback
        self._generators = generators
        frame = tk.Frame(parent)
        frame.pack(fill=tk.X, padx=20, pady=20)
        label = tk.Label(frame, text="Please select a preset generator:")
        label.pack(fill=tk.X, padx=5, pady=5)
        self.selected = tk.StringVar()
        self.generator_cb = ttk.Combobox(frame, textvariable=self.selected)
        # get first 3 letters of every month name
        self.generator_cb["values"] = list(self._generators.values())
        # prevent typing a value
        self.generator_cb["state"] = "readonly"
        # place the widget
        self.generator_cb.pack(fill=tk.X, padx=5, pady=5)
        self.generator_cb.bind("<<ComboboxSelected>>", self.on_selected)

    def on_selected(self, event):
        value = self.generator_cb.get()
        for key in self._generators.keys():
            if self._generators[key] == value:
                self._callback(key)
