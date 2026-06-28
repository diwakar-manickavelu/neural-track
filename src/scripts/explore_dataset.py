from src.datasets.mot17_explorer import MOT17Explorer

explorer = MOT17Explorer("data/MOT17")

print(explorer.list_sequences())

from src.datasets.mot17 import MOT17Sequence

seq = MOT17Sequence(
    "data/MOT17/train/MOT17-02-FRCNN"
)

seq.summary()