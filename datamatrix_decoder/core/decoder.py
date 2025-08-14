def decode_image(self, path):
    decoded = pyzbar.decode(Image.open(path))
    return [obj.type for obj in decoded]

