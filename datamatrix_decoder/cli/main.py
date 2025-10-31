"""Command-line interface for DataMatrix Decoder."""

import sys
import json
from pathlib import Path

import click
from rich.console import Console
from rich.table import Table

from datamatrix_decoder import DataMatrixDecoder, BarcodeDecoder

console = Console()


@click.group()
@click.version_option(version="1.0.0")
def cli():
    """DataMatrix Decoder - Professional barcode decoding tool."""
    pass


@cli.command()
@click.argument("image_path", type=click.Path(exists=True))
@click.option("--format", "-f", default="datamatrix", help="Barcode format")
def decode(image_path: str, format: str):
    """Decode a single image."""
    try:
        if format == "datamatrix":
            decoder = DataMatrixDecoder()
            result = decoder.decode_image(image_path)
            if result:
                console.print(f"[green]✓[/green] Decoded: {result.data}")
            else:
                console.print("[red]✗[/red] No Data Matrix found")
        else:
            decoder = BarcodeDecoder(formats=[format])
            results = decoder.decode_image(image_path)
            if results:
                for result in results:
                    console.print(f"[green]✓[/green] {result.format.upper()}: {result.data}")
            else:
                console.print(f"[red]✗[/red] No barcode found")
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)


@cli.command()
@click.argument("directory", type=click.Path(exists=True))
@click.option("--output", "-o", help="Output JSON file")
@click.option("--workers", "-w", default=4, help="Parallel workers")
def batch(directory: str, output: str, workers: int):
    """Batch process images in a directory."""
    try:
        image_paths = list(Path(directory).glob("*.png")) + list(Path(directory).glob("*.jpg"))
        
        if not image_paths:
            console.print(f"[yellow]No images found in {directory}[/yellow]")
            return
        
        decoder = BarcodeDecoder()
        results = decoder.decode_batch(image_paths, max_workers=workers)
        
        table = Table(title="Decode Results")
        table.add_column("File", style="cyan")
        table.add_column("Format", style="magenta")
        table.add_column("Data", style="green")
        
        for result in results:
            table.add_row(Path(result.filename).name, result.format, result.data)
        
        console.print(table)
        
        if output:
            with open(output, "w") as f:
                json.dump([r.to_dict() for r in results], f, indent=2)
            console.print(f"\n[green]✓[/green] Saved to {output}")
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)


def main():
    """Entry point for CLI."""
    cli()


if __name__ == "__main__":
    main()

# CLI follows single responsibility principle


# CLI provides intuitive user experience

