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

    def make_presets(self):
        for row in range(self.rows):
            for col in range(self.columns):
                for row_ndx in range(self.rows-row):
                    for col_ndx in range(self.columns-col):
                        num_col = col_ndx + 1
                        num_row = row_ndx + 1
                        x, y, w, h = self.calc_block(row, col, num_row, num_col)
                        name =     f"Grid%28{self.columns}x{self.rows}%29-%28{row}%2C{col}%29%28{num_row}x{num_col}%29"
                        preset = "---\n"                    
                        preset += f"rect: {x} {y} {w} {h} 1\n"
                        preset += "radius: 0\n"
                        preset += "color: #00000000\n"
                        preset += "..."
                        path = Path("./presets/cropRectangle") / Path(name)
                        print(path.as_posix())
                        with open(path.as_posix(),"w") as out_file:
                            out_file.write(preset)
                    
        

def main():
    width, height = 1920, 1080
    colums, rows = 3, 2
    grid = Grid(width, height, colums, rows)
    grid.set_padding(9, 16)
    grid.make_presets()
    colums, rows = 3, 3
    grid = Grid(width, height, colums, rows)
    grid.set_padding(9, 16)
    grid.make_presets()
    
if __name__ == "__main__":
    main()
