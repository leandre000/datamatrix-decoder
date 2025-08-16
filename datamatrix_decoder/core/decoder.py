from concurrent.futures import ThreadPoolExecutor, as_completed

def decode_batch(self, paths, workers=4):
    results = []
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(self.decode_image, p): p for p in paths}
        for future in as_completed(futures):
            results.append(future.result())
    return results

