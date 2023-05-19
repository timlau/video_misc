from dataclasses import dataclass
from pathlib import Path
from string import Template
from preset import PresetData, Grid
import urllib

PRESET = """---
rect: $x $y $width $height 1
radius: 0
color: "#00000000"
..."""


@dataclass
class GridPreset:
    data: PresetData
    grid_calc: Grid

    def make_crop_preset(self, row, col, num_col, num_row):
        x, y, w, h = self.grid_calc.calc_block(row, col, num_row, num_col)
        grid = self.grid_calc.grid
        name = f"Grid_{grid.columns}x{grid.rows}_{self.data.video_mode.height}_({row+1},{col+1}.{num_row}x{num_col})"  # noqa
        template = Template(PRESET)
        tpl = template.substitute(
            x=x,
            y=y,
            x_end=x,
            height=h,
            width=w,
        )
        self.write_preset(name, tpl)

    def write_preset(self, name: str, preset: str):
        qf_name = urllib.parse.quote_plus(name)
        directory = Path(self.data.output) / Path("presets/cropRectangle")
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)
        path = directory / Path(qf_name)
        if not path.exists() or self.data.update:
            print(f"create preset {name} : {path.resolve().name}")
            with open(path.resolve(), "w") as out_file:
                out_file.write(preset)
        else:
            print(f" --> {name} : {path.resolve().name} already exist")

    def generate(self):
        grid = self.grid_calc.grid
        for row in range(grid.rows):
            for col in range(grid.columns):
                for row_ndx in range(grid.rows - row):
                    for col_ndx in range(grid.columns - col):
                        num_col = col_ndx + 1
                        num_row = row_ndx + 1
                        self.make_crop_preset(row, col, num_col, num_row)
