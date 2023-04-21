# Padding

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
        if last_col == self.columns:  # lastdx column
            b_x = round(num_col * x_block - self.padding_x)
        else:
            b_x = round(num_col * x_block - (dx))
        if last_row == self.rows:  #  last row
            b_y = round(num_row * y_block - self.padding_y)
        else:
            b_y = round(num_row * y_block - (dy))
        return x, y, b_x, b_y


def main():
    width, height = 1920, 1080
    colums, rows = 3, 2
    grid = Grid(width, height, colums, rows)
    grid.set_padding(9, 16)
    clips = [
        # row 0
        (0, 0, 1, 1),
        (0, 0, 1, 2),
        (0, 0, 1, 3),
        (0, 1, 1, 1),
        (0, 1, 1, 2),
        (0, 2, 1, 1),
        # row 1
        (1, 0, 1, 1),
        (1, 0, 1, 2),
        (1, 0, 1, 3),
        (1, 1, 1, 1),
        (1, 1, 1, 2),
        (1, 2, 1, 1),
    ]

    for row in range(rows):
        for col in range(colums):
            for row_ndx in range(rows-row):
                for col_ndx in range(colums-col):
                    num_col = col_ndx + 1
                    num_row = row_ndx + 1
                    x, y, w, h = grid.calc_block(row, col, num_row, num_col)
                    name =     f"Grid%28{colums}x{rows}%29-%28{row}%2C{col}%29%28{num_row}x{num_col}%29"
                    preset = "---\n"                    
                    preset += f"rect: {x} {y} {w} {h} 1\n"
                    preset += "radius: 0\n"
                    preset += "color: #00000000\n"
                    preset += "..."
                    path = Path("./presets/cropRectangle") / Path(name)
                    with open(path.as_posix(),"w") as out_file:
                        out_file.write(preset)
                    

if __name__ == "__main__":
    main()
