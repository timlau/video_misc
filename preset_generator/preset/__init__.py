from dataclasses import dataclass
from functools import cached_property
from pathlib import Path


@dataclass
class VideoMode:
    width: int
    height: int
    fps: int


@dataclass
class Grid:
    columns: int
    rows: int
    padding: int


@dataclass
class SlideIn:
    size: int = 2
    duration: int = 7


@dataclass
class PresetData:
    # video mode
    video_mode: VideoMode
    # grid
    grid: Grid
    # slide in
    slide_in: SlideIn
    # generel
    preset: str = "grid"
    output: Path = Path.home() / Path("Documents") / Path("Shotcut")
    update: bool = True


@dataclass
class GridCalc:
    video_mode: VideoMode
    grid: Grid

    @cached_property
    def grid_width(self):
        return round(self.video_mode.width / self.grid.columns)

    @cached_property
    def grid_height(self):
        return round(self.video_mode.height / self.grid.rows)

    def calc_block(self, start_row, start_col, num_row, num_col, border: bool = True):
        last_col = start_col + num_col
        last_row = start_row + num_row
        if border:
            dt = self.grid.padding / 2
            extra = 0
        else:
            dt = 0
            # if no border we need to add extra to width & height
            extra = self.grid.padding / 2
        x = round(dt + (start_col * self.grid_width))
        y = round(dt + (start_row * self.grid_height))
        if last_col == self.grid.columns:
            width = round(num_col * self.grid_width - (2 * dt)) + extra
        else:
            width = round(num_col * self.grid_width - (dt)) + extra
        if last_row == self.grid.rows:
            height = round(num_row * self.grid_height - (2 * dt)) + extra
        else:
            height = round(num_row * self.grid_height - (dt)) + extra
        return x, y, width, height


def grid_from_preset(data: PresetData) -> GridCalc:
    return GridCalc(
        video_mode=data.video_mode,
        grid=data.grid,
    )


def create_default_preset_data() -> PresetData:
    video_mode = VideoMode(
        width=1920,
        height=1080,
        fps=30,
    )
    grid = Grid(
        rows=3,
        columns=3,
        padding=16,
    )
    slide_in = SlideIn(
        size=2,
        duration=7,
    )
    return PresetData(video_mode=video_mode, grid=grid, slide_in=slide_in)
