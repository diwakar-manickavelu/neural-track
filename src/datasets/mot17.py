from pathlib import Path
import configparser
import pandas as pd
import cv2


class MOT17Sequence:

    def __init__(self, sequence_path):

        self.sequence_path = Path(sequence_path)

        # ---------- Read sequence info ----------
        self.config = configparser.ConfigParser()
        self.config.read(self.sequence_path / "seqinfo.ini")

        self.name = self.config["Sequence"]["name"]
        self.length = int(self.config["Sequence"]["seqLength"])
        self.width = int(self.config["Sequence"]["imWidth"])
        self.height = int(self.config["Sequence"]["imHeight"])
        self.fps = int(self.config["Sequence"]["frameRate"])

        # ---------- Load annotations ----------
        self.gt = pd.read_csv(
            self.sequence_path / "gt" / "gt.txt",
            header=None
        )

        self.det = pd.read_csv(
            self.sequence_path / "det" / "det.txt",
            header=None
        )

    def summary(self):

        print(f"Sequence : {self.name}")
        print(f"Frames   : {self.length}")
        print(f"Resolution : {self.width} x {self.height}")
        print(f"FPS      : {self.fps}")

    def load_frame(self, frame):

        filename = f"{frame:06d}.jpg"

        return cv2.imread(
            str(self.sequence_path / "img1" / filename)
        )

    def get_ground_truth(self, frame):

        return self.gt[self.gt[0] == frame]

    def get_detections(self, frame):

        return self.det[self.det[0] == frame]