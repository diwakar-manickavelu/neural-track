from pathlib import Path


class MOT17Explorer:

    def __init__(self, root):
        self.root = Path(root)

    def list_sequences(self):
        train = self.root / "train"
        return sorted([p.name for p in train.iterdir() if p.is_dir()])