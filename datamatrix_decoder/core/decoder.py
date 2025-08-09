from PIL import Image
from pylibdmtx.pylibdmtx import decode

class DataMatrixDecoder:
    def __init__(self):
        self.timeout = 30
    
    def decode_image(self, path):
        img = Image.open(path)
        return decode(img)

