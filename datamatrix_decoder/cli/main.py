@click.option('--output', '-o')
def decode(image_path, output):
    if output:
        with open(output, 'w') as f:
            json.dump(results, f)

