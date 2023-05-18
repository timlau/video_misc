from dataclasses import dataclass
from pathlib import Path
from PyQt6.QtCore import QObject, pyqtProperty, pyqtSlot, pyqtSignal


@dataclass
class UIData:
    width: int = 1920
    height: int = 1080
    fps: int = 30
    rows: int = 3
    columns: int = 3
    padding: int = 16
    size: int = 2
    duration: int = 5
    preset: str = "grid"
    output: Path = Path(".") / Path("Shotcut")


class Backend(QObject):
    refresh = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.data = UIData()

    @pyqtSlot()
    def generate(self):
        print("Generate")
        print(self.data)

    @pyqtProperty(str)
    def preset(self):
        return self.data.preset

    @preset.setter
    def preset(self, value):
        self.data.preset = value
        self.refresh.emit(value)

    @pyqtProperty(str)
    def output_dir(self):
        return str(self.data.output.resolve())

    @output_dir.setter
    def output_dir(self, value):
        self.data.output = Path(value)

    @pyqtProperty(str)
    def video_width(self):
        return str(self.data.width)

    @video_width.setter
    def video_width(self, value):
        if value:
            self.data.width = int(value)

    @pyqtProperty(str)
    def video_height(self):
        return str(self.data.height)

    @video_height.setter
    def video_height(self, value):
        if value:
            self.data.height = int(value)

    @pyqtProperty(str)
    def video_fps(self):
        return str(self.data.fps)

    @video_fps.setter
    def video_fps(self, value):
        if value:
            self.data.fps = int(value)

    @pyqtProperty(str)
    def grid_rows(self):
        return str(self.data.rows)

    @grid_rows.setter
    def grid_rows(self, value):
        if value:
            self.data.rows = int(value)

    @pyqtProperty(str)
    def grid_cols(self):
        return str(self.data.columns)

    @grid_cols.setter
    def grid_cols(self, value):
        if value:
            self.data.columns = int(value)

    @pyqtProperty(str)
    def grid_pad(self):
        return str(self.data.padding)

    @grid_pad.setter
    def grid_pad(self, value):
        if value:
            self.data.padding = int(value)

    @pyqtProperty(str)
    def slide_size(self):
        return str(self.data.size)

    @slide_size.setter
    def slide_size(self, value):
        if value:
            self.data.size = int(value)

    @pyqtProperty(str)
    def slide_duration(self):
        return str(self.data.duration)

    @slide_duration.setter
    def slide_duration(self, value):
        if value:
            self.data.duration = int(value)
