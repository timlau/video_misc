from dataclasses import dataclass


FONT_NORMAL = ("Noto Sans", 10)
FONT_BOLD = ("Noto Sans", 10, "bold")


@dataclass
class VideoMode:
    width: int
    height: int
    fps: int

    def __str__(self) -> str:
        return f"{self.width}x{self.height} FPS:{self.fps}"


@dataclass
class Grid:
    rows: int
    columns: int
    padding: int
