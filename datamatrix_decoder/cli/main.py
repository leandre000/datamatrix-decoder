from rich.progress import track

for item in track(items):
    process(item)

