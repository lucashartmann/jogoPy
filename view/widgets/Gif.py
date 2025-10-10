from PIL import Image
from PIL.Image import Resampling
from textual.widget import Widget
from textual.timer import Timer
from textual.widgets import Static
from textual_image.widget import Image as TextualImage
from rich_pixels import Pixels
from textual.containers import Container


class Gif(Static):
    def __init__(self, aseprite_path, pixel=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pixel = pixel
        self.frames, self.durations = self.extract_frames_from_aseprite(
            aseprite_path)
        self.sprite = aseprite_path
        self.frame_index = 0
        self.timer: Timer | None = None
        self.paused = False

    def set_sprite(self, caminho):
        self.sprite = caminho
        self.frames, self.durations = self.extract_frames_from_aseprite(
            caminho)

    @staticmethod
    def extract_frames_from_aseprite(sheet_path: str, frame_width=64, frame_height=64):
        sheet = Image.open(sheet_path)
        sheet_width, sheet_height = sheet.size

        frames = []
        durations = []

        cols = sheet_width // frame_width

        for x in range(cols):
            box = (
                x * frame_width + 24,
                18,
                (x + 1) * frame_width,
                frame_height
            )
            frame = sheet.crop(box)
            frame = frame.resize((40, 40), resample=Resampling.NEAREST)
            frames.append(frame)
            durations.append(110)

        return frames, durations

    

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
            self.update(Pixels.from_image(frame))
        

        self.timer.pause()
        self.timer.resume()
