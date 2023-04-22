# Padding

import urllib
import argparse
from dataclasses import dataclass
from pathlib import Path

from regex import FULLCASE


@dataclass
class Grid:
    width: int
    height: int
    columns: int
    rows: int
    update: bool
    output: str
    xpad: int
    ypad: int

    @property
    def block_size(self):
        block_width = round(self.width / self.columns)
        block_height = round(self.height / self.rows)
        return block_width, block_height

    def set_padding(self, x, y):
        self.xpad = x
        self.ypad = y

    def calc_block(self, row, col, num_row, num_col):
        x_block, y_block = self.block_size
        last_col = col + num_col
        last_row = row + num_row
        dx = self.xpad / 2
        dy = self.ypad / 2
        x = round(dx + (col * x_block))
        y = round(dy + (row * y_block))
        if last_col == self.columns:
            b_x = round(num_col * x_block - self.xpad)
        else:
            b_x = round(num_col * x_block - (dx))
        if last_row == self.rows:
            b_y = round(num_row * y_block - self.ypad)
        else:
            b_y = round(num_row * y_block - (dy))
        return x, y, b_x, b_y

    def make_presets(self):
        for row in range(self.rows):
            for col in range(self.columns):
                for row_ndx in range(self.rows - row):
                    for col_ndx in range(self.columns - col):
                        num_col = col_ndx + 1
                        num_row = row_ndx + 1
                        self.write_crop_preset(row, col, num_col, num_row)

    def write_crop_preset(self, row, col, num_col, num_row):
        x, y, w, h = self.calc_block(row, col, num_row, num_col)
        name = f"Grid_{self.columns}x{self.rows}_{self.height}_({row+1},{col+1}.{num_row}x{num_col})"
        qf_name = urllib.parse.quote_plus(name)
        preset = "---\n"
        preset += f"rect: {x} {y} {w} {h} 1\n"
        preset += "radius: 0\n"
        preset += 'color: "#00000000"\n'
        preset += "..."
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
        prog="pyhton create_grid_presets.py",
        description="Create preset for crop: rectangle filter in Shotcut",
    )
    parser.add_argument("--width", type=int, default=1920, help="Frame Width (Default: 1940)")
    parser.add_argument("--height", type=int, default=1080, help="Frame Height (Default: 1080)")
    parser.add_argument("columns", type=int, help="Number of grid colums")
    parser.add_argument("rows", type=int, help="Number of grid rows")
    parser.add_argument("--xpad", type=int, default=15, help="padding between columns (default: 15px)")
    parser.add_argument("--ypad", type=int, default=15,help="padding between rows")
    parser.add_argument("--update", default=False, action="store_true",help="Update existing presets")
    parser.add_argument("-o", "--output", type=str, default=".", help="output directory (default: current dir)")

    args = parser.parse_args()
    kwargs = vars(args)
    print(kwargs)
    grid = Grid(**kwargs)
    grid.make_presets()


if __name__ == "__main__":
    main()
