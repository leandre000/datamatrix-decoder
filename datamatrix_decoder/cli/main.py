import click

@click.command()
@click.argument('image_path')
def decode(image_path):
    print(f'Decoding {image_path}')

