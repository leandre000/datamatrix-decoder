from concurrent.futures import ThreadPoolExecutor

def decode_batch(self, paths, workers=4):
    with ThreadPoolExecutor(max_workers=workers) as executor:
        pass

