# Padding

import urllib
import argparse
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Grid:
    width: int
    height: int
    columns: int
    rows: int
    padding_x = 0
    padding_y = 0

    @property
    def block_size(self):
        block_width = round(self.width / self.columns)
        block_height = round(self.height / self.rows)
        return block_width, block_height

    def set_padding(self, x, y):
        self.padding_x = x
        self.padding_y = y

    def calc_block(self, row, col, num_row, num_col):
        x_block, y_block = self.block_size
        last_col = col + num_col
        last_row = row + num_row
        dx = self.padding_x / 2
        dy = self.padding_y / 2
        x = round(dx + (col * x_block))
        y = round(dy + (row * y_block))
        if last_col == self.columns:
            b_x = round(num_col * x_block - self.padding_x)
        else:
            b_x = round(num_col * x_block - (dx))
        if last_row == self.rows:
            b_y = round(num_row * y_block - self.padding_y)
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
                        x, y, w, h = self.calc_block(row, col, num_row, num_col)
                        name = f"Grid({self.columns}x{self.rows})-({row},{col})({num_row}x{num_col})"
                        qf_name = urllib.parse.quote_plus(name)
                        preset = "---\n"
                        preset += f"rect: {x} {y} {w} {h} 1\n"
                        preset += "radius: 0\n"
                        preset += "color: #00000000\n"
                        preset += "..."
                        path = Path("./presets/cropRectangle") / Path(qf_name)
                        if not path.exists():
                            print(f"create preset {name} : {path.resolve().name}")
                            with open(path.resolve(), "w") as out_file:
                                out_file.write(preset)
                        else:
                            print(f" --> {name} : {path.resolve().name} already exist")


def main():
    parser = argparse.ArgumentParser(
        prog="create_grid_preset",
        description="Create preset for crop: rectangle filter in Shotcut",
    )
    parser.add_argument("width", type=int)
    parser.add_argument("height", type=int)
    parser.add_argument("columns", type=int)
    parser.add_argument("rows", type=int)
    parser.add_argument("--xpad", type=int, default=9)
    parser.add_argument("--ypad", type=int, default=16)

    args = parser.parse_args()

    width, height = args.width, args.height
    colums, rows = args.columns, args.rows
    grid = Grid(width, height, colums, rows)
    grid.set_padding(args.xpad, args.ypad)
    grid.make_presets()


if __name__ == "__main__":
    main()
