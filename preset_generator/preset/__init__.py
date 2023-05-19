from dataclasses import dataclass
from pathlib import Path


@dataclass
class PresetData:
    # video mode
    width: int = 1920
    height: int = 1080
    fps: int = 30
    # grid
    rows: int = 3
    columns: int = 3
    padding: int = 16
    # slide in
    size: int = 2
    duration: int = 7
    # generel
    preset: str = "grid"
    output: Path = Path.home() / Path("Documents") / Path("Shotcut")
    update: bool = True


@dataclass
class Grid:
    width: int
    height: int
    columns: int
    rows: int
    update: bool
    xpad: int
    ypad: int

    @property
    def grid_width(self):
        return round(self.width / self.columns)

    @property
    def grid_height(self):
        return round(self.height / self.rows)

    @property
    def block_size(self):
        return self.grid_width, self.grid_height

    def set_padding(self, x, y):
        self.xpad = x
        self.ypad = y

    def calc_block(self, start_row, start_col, num_row, num_col, border: bool = True):
        grid_width, grid_height = self.block_size
        last_col = start_col + num_col
        last_row = start_row + num_row
        if border:
            dx = self.xpad / 2
            dy = self.ypad / 2
            extra_w = extra_h = 0
        else:
            dx = dy = 0
            # if no border we need to add extra to width & height
            extra_w = self.xpad / 2
            extra_h = self.ypad / 2
        x = round(dx + (start_col * grid_width))
        y = round(dy + (start_row * grid_height))
        if last_col == self.columns:
            width = round(num_col * grid_width - (2 * dx)) + extra_w
        else:
            width = round(num_col * grid_width - (dx)) + extra_w
        if last_row == self.rows:
            height = round(num_row * grid_height - (2 * dy)) + extra_h
        else:
            height = round(num_row * grid_height - (dy)) + extra_h
        return x, y, width, height


def grid_from_preset_data(data: PresetData):
    return Grid(
        width=data.width,
        height=data.height,
        columns=data.columns,
        rows=data.rows,
        update=data.update,
        xpad=data.padding,
        ypad=data.padding,
    )
