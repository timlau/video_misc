import tkinter as tk

from ui.elements import VideoModeUI, GridSizeUI, OutputUI, SlideUI, Selector

GENERATORS = {
    "grid": "Crop Rectangle : Grid",
    "slidein": "Crop Rectangle : Corner Slide",
}


class Application:
    def __init__(self):
        self.active = None
        self.app = tk.Tk()
        self.app.geometry("800x600")
        self.app.title("Shotcut Preset Generator")
        self.content = tk.Frame(
            self.app, highlightbackground="black", highlightthickness=1
        )
        self.content.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=5, pady=5)

        _ = Selector(self.content, GENERATORS, callback=self.on_generator_selected)
        self.sub_content = tk.Frame(self.content)
        self.sub_content.pack(fill=tk.X, padx=20, pady=20)
        btn1 = tk.Button(self.content, text="Build", command=self.on_build)
        btn1.pack(side=tk.BOTTOM, pady=20)
        self.app.mainloop()

    def on_build(self):
        if self.active:
            match self.active:
                case "grid":
                    print(self.video_mode.read_values())
                    print(self.grid_size.read_values())
                    print(self.output.read_values())
                case "slidein":
                    print(self.video_mode.read_values())
                    print(self.grid_size.read_values())
                    print(self.slide.read_values())
                    print(self.output.read_values())

    def on_generator_selected(self, value: str):
        self.active = value
        self.sub_content.destroy()
        self.sub_content = tk.Frame(
            self.content, highlightbackground="black", highlightthickness=1
        )

        self.sub_content.pack(fill=tk.X, padx=20, pady=5)

        row = 1
        match value:
            case "grid":
                self.video_mode = VideoModeUI(self.sub_content, row)
                row += 2
                self.grid_size = GridSizeUI(self.sub_content, row)
                row += 2
                self.output = OutputUI(self.sub_content, row)
            case "slidein":
                self.video_mode = VideoModeUI(self.sub_content, row)
                row += 2
                self.grid_size = GridSizeUI(self.sub_content, row)
                row += 2
                self.slide = SlideUI(self.sub_content, row)
                row += 2
                self.output = OutputUI(self.sub_content, row)


if __name__ == "__main__":
    Application()
