from PIL import Image

class DataMatrixDecoder:
    def __init__(self):
        self.timeout = 30
    
    def load_image(self, path):
        return Image.open(path)

