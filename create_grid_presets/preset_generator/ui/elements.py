import tkinter as tk

from tkinter import ttk
from pathlib import Path

from ui import FONT_BOLD, VideoMode, Grid
from ui.widgets import GridEntry, PackEntry


class VideoModeUI:
    def __init__(self, parent) -> None:
        frame = tk.Frame(parent, highlightbackground="black", highlightthickness=1)
        frame.pack(fill=tk.X, padx=20, pady=5)
        frame.columnconfigure(0, weight=0)
        frame.columnconfigure(1, weight=0)
        frame.columnconfigure(2, weight=0)
        frame.columnconfigure(3, weight=0)
        frame.columnconfigure(4, weight=0)
        frame.columnconfigure(5, weight=0)
        label = tk.Label(frame, text="Video Mode", font=FONT_BOLD)
        label.grid(row=0, column=0, pady=5, padx=5)
        self.width = GridEntry(frame, "Width", default="1920", row=1, col=0)
        self.height = GridEntry(frame, "Height", default="1080", row=1, col=2)
        self.fps = GridEntry(frame, "FPS", default="30", row=1, col=4)

    def read_values(self) -> VideoMode:
        width = int(self.width.entry.get())
        height = int(self.height.entry.get())
        fps = int(self.fps.entry.get())
        return VideoMode(height=height, width=width, fps=fps)


class GridSizeUI:
    def __init__(self, parent) -> None:
        frame = tk.Frame(parent, highlightbackground="black", highlightthickness=1)
        frame.pack(fill=tk.X, padx=20, pady=5)
        frame.columnconfigure(0, weight=0)
        frame.columnconfigure(1, weight=0)
        frame.columnconfigure(2, weight=0)
        frame.columnconfigure(3, weight=0)
        frame.columnconfigure(4, weight=0)
        frame.columnconfigure(5, weight=0)
        label = tk.Label(frame, text="Grid_Size", font=FONT_BOLD)
        label.grid(row=0, column=0, pady=5, padx=5)
        self.rows = GridEntry(frame, "Rows", default="3", row=1, col=0)
        self.columns = GridEntry(frame, "Columns", default="3", row=1, col=2)
        self.padding = GridEntry(frame, "Padding", default="16", row=1, col=4)

    def read_values(self):
        rows = int(self.rows.entry.get())
        columns = int(self.columns.entry.get())
        padding = int(self.padding.entry.get())
        return Grid(rows=rows, columns=columns, padding=padding)


class SlideUI:
    def __init__(self, parent) -> None:
        frame = tk.Frame(parent, highlightbackground="black", highlightthickness=1)
        frame.pack(fill=tk.X, padx=20, pady=5)
        frame.columnconfigure(0, weight=0)
        frame.columnconfigure(1, weight=0)
        frame.columnconfigure(2, weight=0)
        frame.columnconfigure(3, weight=0)
        frame.columnconfigure(4, weight=0)
        frame.columnconfigure(5, weight=0)
        label = tk.Label(frame, text="Slide", font=FONT_BOLD)
        label.grid(row=0, column=0, pady=5, padx=5)
        self.size = GridEntry(frame, "Size", default="2", row=1, col=0)
        self.duration = GridEntry(frame, "Duration", default="5", row=1, col=2)


class OutputUI:
    def __init__(self, parent) -> None:
        frame = tk.Frame(parent, highlightbackground="black", highlightthickness=1)
        frame.pack(fill=tk.X, padx=20, pady=5)
        self.output = PackEntry(frame, "Output directory", default=".")

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