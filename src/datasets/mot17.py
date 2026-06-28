from pathlib import Path
import configparser


class MOT17Sequence:

    def __init__(self, sequence_path):

        self.sequence_path = Path(sequence_path)

        self.config = configparser.ConfigParser()
        self.config.read(self.sequence_path / "seqinfo.ini")

        self.name = self.config["Sequence"]["name"]
        self.length = int(self.config["Sequence"]["seqLength"])
        self.width = int(self.config["Sequence"]["imWidth"])
        self.height = int(self.config["Sequence"]["imHeight"])
        self.fps = int(self.config["Sequence"]["frameRate"])

    def summary(self):

        print(f"Sequence : {self.name}")
        print(f"Frames   : {self.length}")
        print(f"Size     : {self.width} x {self.height}")
        print(f"FPS      : {self.fps}")