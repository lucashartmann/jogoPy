import subprocess
import json
from PIL import Image
from textual.widget import Widget
from textual.timer import Timer
from textual.widgets import Static
from textual_image.widget import Image as TextualImage
from textual.containers import VerticalGroup
from rich_pixels import Pixels

class Gif(Widget):
    def __init__(self, aseprite_path, pixel=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pixel = pixel
        self.frames, self.durations = self.extract_frames_from_aseprite(
            aseprite_path)
        self.sprite = aseprite_path
        self.frame_index = 0
        self.timer: Timer | None = None
        self.paused = False

    @staticmethod
    def extract_frames_from_aseprite(aseprite_file: str, output_prefix="temp"):
        sheet_path = f"{output_prefix}.png"
        data_path = f"{output_prefix}.json"

        subprocess.run([
            "aseprite", "-b", aseprite_file,
            "--sheet", sheet_path,
            "--data", data_path,
            "--sheet-pack",
            "--format", "json-array"
        ], check=True)

        sheet = Image.open(sheet_path)
        with open(data_path, "r") as f:
            data = json.load(f)

        frames = []
        durations = []

        for frame_info in data["frames"]:
            rect = frame_info["frame"]
            duration = frame_info["duration"]
            box = (
                rect["x"],
                rect["y"],
                rect["x"] + rect["w"],
                rect["y"] + rect["h"]
            )
            frame = sheet.crop(box)
            frames.append(frame)
            durations.append(duration)

        return frames, durations

    def compose(self):
        with VerticalGroup(id="video_container"):
            if self.pixel:
                yield Static(Pixels.from_image(self.frames[0]), id="video_pixels")
            else:
                yield TextualImage(self.frames[0])

    def on_mount(self):
        self.start()

    def start(self):
        self.timer = self.set_interval(
            self._current_interval(), self.update_frame)

    def pause(self):
        if not self.timer:
            self.start()
        else:
            if self.paused:
                self.timer.resume()
                self.paused = False
            else:
                self.timer.pause()
                self.paused = True

    def _current_interval(self):
        return self.durations[self.frame_index] / 1000 

    def update_frame(self):
        self.frame_index = (self.frame_index + 1) % len(self.frames)
        frame = self.frames[self.frame_index]

        if self.pixel:
            self.query_one(Static).update(Pixels.from_image(frame))
        else:
            self.query_one(TextualImage).image = frame

        self.timer.pause()
        self.timer.set_interval(self._current_interval())
        self.timer.resume()
