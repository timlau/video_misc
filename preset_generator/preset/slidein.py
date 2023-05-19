import urllib
from dataclasses import dataclass
from pathlib import Path

from string import Template

from preset import GridCalc, PresetData

PRESET = """---
rect: 0=$x_start $y_start 0 0 1;$frame_in=$x_end $y_end $width $height 1;$frame_out=$x_end $y_end $width $height 1;$frame_end=$x_start $y_start 0 0 1
radius: 0=0;$frame_in=0;$frame_out=0;$frame_end=0
color: "#00000000"
"shotcut:animIn": "00:00:01.000"
"shotcut:animOut": "00:00:01.000"
..."""  # noqa

PRESET_BORDER = """---
rect: 0|=0 0 0 0 1;$frame_in|=$x_end $y_end $width $height 1;$frame_out|=0 0 0 0 1
radius: 0
color: "#00000000"
"shotcut:animIn": "00:00:00.000"
"shotcut:animOut": "00:00:00.000"
..."""


@dataclass
class SlideInPreset:
    data: PresetData
    grid_calc: GridCalc

    @property
    def video_mode(self):
        return self.data.video_mode

    @property
    def slide_in(self):
        return self.data.slide_in

    @property
    def frame_end(self):
        return (self.slide_in.duration * self.video_mode.fps) - 1

    @property
    def frame_in(self):
        return self.video_mode.fps - 1

    @property
    def frame_out(self):
        return self.frame_end - self.video_mode.fps + 1

    @property
    def filename(self):
        return f"{self.video_mode.height}p_{self.video_mode.fps}fps_{self.slide_in.duration}s_{self.slide_in.size}x{self.slide_in.size}"  # noqa

    def calc_top_left(self, border: bool = True):
        x, y, w, h = self.grid_calc.calc_block(
            0, 0, self.slide_in.size, self.slide_in.size, border=border
        )
        prefix = "SlideIn_TL"
        if not border:
            prefix += "_B"
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
        self.write_preset(f"{prefix}_{self.filename}", tpl)

    def calc_top_right(self, border: bool = True):
        x, y, w, h = self.grid_calc.calc_block(
            0, 1, self.slide_in.size, self.slide_in.size, border=border
        )
        prefix = "SlideIn_TR"
        if not border:
            prefix += "_B"
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
        self.write_preset(f"{prefix}_{self.filename}", tpl)

    def calc_bottom_left(self, border: bool = True):
        x, y, w, h = self.grid_calc.calc_block(
            1, 0, self.slide_in.size, self.slide_in.size, border=border
        )
        prefix = "SlideIn_BL"
        if not border:
            prefix += "_B"
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
        self.write_preset(f"{prefix}_{self.filename}", tpl)

    def calc_bottom_right(self, border: bool = True):
        x, y, w, h = self.grid_calc.calc_block(
            1, 1, self.slide_in.size, self.slide_in.size, border=border
        )
        prefix = "SlideIn_BR"
        if not border:
            prefix += "_B"
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
        self.write_preset(f"{prefix}_{self.filename}", tpl)

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
        self.calc_top_left()
        self.calc_top_left(border=False)
        self.calc_top_right()
        self.calc_top_right(border=False)
        self.calc_bottom_left()
        self.calc_bottom_left(border=False)
        self.calc_bottom_right()
        self.calc_bottom_right(border=False)
