from PIL import Image
from pathlib import Path

class DataMatrixDecoder:
    def decode_image(self, path):
        if not Path(path).exists():
            raise FileNotFoundError(path)
        return None

