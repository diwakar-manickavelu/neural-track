from src.datasets.mot17 import MOT17Sequence

from pathlib import Path

from config import MOT17_DIR

seq = MOT17Sequence(MOTI7_DIR / "train" / "MOT17-02-FRCNN")

seq.summary()

image = seq.load_frame(1)

print(image.shape)

print(seq.get_ground_truth(1).head())

print(seq.get_detections(69).head())