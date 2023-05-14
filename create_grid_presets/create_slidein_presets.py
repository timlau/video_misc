import argparse
import urllib
from dataclasses import dataclass
from pathlib import Path

from string import Template

PRESET = """---
rect: 0=$x_start $y_start 0 0 1;$frame_in=$x_end $y_end $width $height 1;$frame_out=$x_end $y_end $width $height 1;$frame_end=$x_start $y_start 0 0 1
radius: 0=0;$frame_in=0;$frame_out=0;$frame_end=0
color: "#00000000"
"shotcut:animIn": "00:00:01.000"
"shotcut:animOut": "00:00:01.000"
..."""

PRESET_BORDER = """---
rect: 0|=0 0 0 0 1;$frame_in|=$x_end $y_end $width $height 1;$frame_out|=0 0 0 0 1
radius: 0
color: "#00000000"
"shotcut:animIn": "00:00:00.000"
"shotcut:animOut": "00:00:00.000"
..."""

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


@dataclass
class Preset:
    grid: Grid
    size: int
    fps: int
    duration: int

    def set_output(self, output: str, update: bool):
        self.output = output
        self.update = update

    @property
    def frame_end(self):
        return (self.duration * self.fps) - 1

    @property
    def frame_in(self):
        return self.fps - 1

    @property
    def frame_out(self):
        return self.frame_end - self.fps + 1

    def calc_top_left(self, border: bool = True):
        x, y, w, h = self.grid.calc_block(0, 0, self.size, self.size, border=border)
        prefix = "SlideIn_Top_Left"
        if not border:
            prefix += "_Border"
            template = Template(PRESET_BORDER)
        else:
            template = Template(PRESET)
        tpl = template.substitute(
            x_start=x,
            y_start=y,
            x_end=x,
            y_end=y,
            frame_in=self.frame_in,
            frame_out=self.frame_out,
            frame_end=self.frame_end,
            height=h,
            width=w,
        )
        self.write_preset(f"{prefix}_{self.grid.height}p_{self.fps}fps", tpl)

    def calc_top_right(self, border: bool = True):
        x, y, w, h = self.grid.calc_block(0, 1, self.size, self.size, border=border)
        prefix = "SlideIn_Top_Right"
        if not border:
            prefix += "_Border"
            template = Template(PRESET_BORDER)
        else:
            template = Template(PRESET)
        tpl = template.substitute(
            x_start=x + w,
            y_start=y,
            x_end=x,
            y_end=y,
            frame_in=self.frame_in,
            frame_out=self.frame_out,
            frame_end=self.frame_end,
            height=h,
            width=w,
        )
        self.write_preset(f"{prefix}_{self.grid.height}p_{self.fps}fps", tpl)

    def calc_bottom_left(self, border: bool = True):
        x, y, w, h = self.grid.calc_block(1, 0, self.size, self.size, border=border)
        prefix = "SlideIn_Bottom_Left"
        if not border:
            prefix += "_Border"
            template = Template(PRESET_BORDER)
        else:
            template = Template(PRESET)
        tpl = template.substitute(
            x_start=x,
            y_start=y + h,
            x_end=x,
            y_end=y,
            frame_in=self.frame_in,
            frame_out=self.frame_out,
            frame_end=self.frame_end,
            height=h,
            width=w,
        )
        self.write_preset(f"{prefix}_{self.grid.height}p_{self.fps}fps", tpl)

    def calc_bottom_right(self, border: bool = True):
        x, y, w, h = self.grid.calc_block(1, 1, self.size, self.size, border=border)
        prefix = "SlideIn_Bottom_Right"
        if not border:
            prefix += "_Border"
            template = Template(PRESET_BORDER)
        else:
            template = Template(PRESET)
        tpl = template.substitute(
            x_start=x + w,
            y_start=y + h,
            x_end=x,
            y_end=y,
            frame_in=self.frame_in,
            frame_out=self.frame_out,
            frame_end=self.frame_end,
            height=h,
            width=w,
        )
        self.write_preset(f"{prefix}_{self.grid.height}p_{self.fps}fps", tpl)

    def write_preset(self, name: str, preset: str):
        qf_name = urllib.parse.quote_plus(name)
        directory = Path(self.output) / Path("presets/cropRectangle")
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)
        path = directory / Path(qf_name)
        if not path.exists() or self.update:
            print(f"create preset {name} : {path.resolve().name}")
            with open(path.resolve(), "w") as out_file:
                out_file.write(preset)
        else:
            print(f" --> {name} : {path.resolve().name} already exist")


def main():
    parser = argparse.ArgumentParser(
        prog="pyhton create_slide_presets.py",
        description="Create preset for crop: rectangle filter in Shotcut",
    )
    parser.add_argument(
        "--width", type=int, default=1920, help="Frame Width (Default: 1940)"
    )
    parser.add_argument(
        "--height", type=int, default=1080, help="Frame Height (Default: 1080)"
    )
    parser.add_argument("columns", type=int, help="Number of grid colums")
    parser.add_argument("rows", type=int, help="Number of grid rows")
    parser.add_argument(
        "--xpad", type=int, default=16, help="padding between columns (default: 15px)"
    )
    parser.add_argument("--ypad", type=int, default=16, help="padding between rows")
    parser.add_argument(
        "--update", default=False, action="store_true", help="Update existing presets"
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default=".",
        help="output directory (default: current dir)",
    )
    parser.add_argument("--fps", type=int, help="Frames per second", default=30)
    parser.add_argument("--size", type=int, help="Size in grid elements", default=1)

    args = parser.parse_args()
    kwargs = vars(args)
    output = kwargs.pop("output")
    fps = kwargs.pop("fps")
    size = kwargs.pop("size")
    grid = Grid(**kwargs)
    preset = Preset(grid=grid, size=size, fps=fps, duration=7)
    preset.set_output(output=output, update=args.update)
    preset.calc_top_left()
    preset.calc_top_left(border=False)
    preset.calc_top_right()
    preset.calc_top_right(border=False)
    preset.calc_bottom_left()
    preset.calc_bottom_left(border=False)
    preset.calc_bottom_right()
    preset.calc_bottom_right(border=False)


if __name__ == "__main__":
    main()
