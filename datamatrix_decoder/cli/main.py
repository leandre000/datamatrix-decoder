import click

@click.command()
@click.argument('directory')
def batch(directory):
    print(f'Batch processing {directory}')

