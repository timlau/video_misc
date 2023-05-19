from pathlib import Path
from PyQt6.QtCore import QObject, pyqtProperty, pyqtSlot, pyqtSignal
from preset import PresetData, create_default_preset_data, grid_from_preset
from preset.slidein import SlideInPreset
from preset.grid import GridPreset


class Builder:
    def __init__(self, data: PresetData):
        self.data = data
        self.grid_calc = grid_from_preset(data)

    def build(self):
        match self.data.preset:
            case "grid":
                preset = GridPreset(data=self.data, grid_calc=self.grid_calc)
                preset.generate()
            case "slide":
                preset = SlideInPreset(data=self.data, grid_calc=self.grid_calc)
                preset.generate()


class Backend(QObject):
    refresh = pyqtSignal(str)
    message = pyqtSignal(str)

    def __init__(self, win):
        super().__init__()
        self.data = create_default_preset_data()
        self.app = win

    @pyqtSlot()
    def generate(self):
        print("Generate")
        print(self.data)
        builder = Builder(self.data)
        builder.build()
        self.message.emit("Presets generated")

    #
    # qml properties
    #

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
        return str(self.data.video_mode.width)

    @video_width.setter
    def video_width(self, value):
        if value:
            self.data.video_mode.width = int(value)

    @pyqtProperty(str)
    def video_height(self):
        return str(self.data.video_mode.height)

    @video_height.setter
    def video_height(self, value):
        if value:
            self.data.video_mode.height = int(value)

    @pyqtProperty(str)
    def video_fps(self):
        return str(self.data.video_mode.fps)

    @video_fps.setter
    def video_fps(self, value):
        if value:
            self.data.video_mode.fps = int(value)

    @pyqtProperty(str)
    def grid_rows(self):
        return str(self.data.grid.rows)

    @grid_rows.setter
    def grid_rows(self, value):
        if value:
            self.data.grid.rows = int(value)

    @pyqtProperty(str)
    def grid_cols(self):
        return str(self.data.grid.columns)

    @grid_cols.setter
    def grid_cols(self, value):
        if value:
            self.data.grid.columns = int(value)

    @pyqtProperty(str)
    def grid_pad(self):
        return str(self.data.grid.padding)

    @grid_pad.setter
    def grid_pad(self, value):
        if value:
            self.data.grid.padding = int(value)

    @pyqtProperty(str)
    def slide_size(self):
        return str(self.data.slide_in.size)

    @slide_size.setter
    def slide_size(self, value):
        if value:
            self.data.slide_in.size = int(value)

    @pyqtProperty(str)
    def slide_duration(self):
        return str(self.data.slide_in.duration)

    @slide_duration.setter
    def slide_duration(self, value):
        if value:
            self.data.slide_in.duration = int(value)
