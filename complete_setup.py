#!/usr/bin/env python3
"""Complete the project setup by adding missing decoder files."""

from pathlib import Path


def create_file(path, content):
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content, encoding='utf-8')
    print(f"✓ Created: {file_path.relative_to(Path.cwd())}")


def main():
    base = Path(__file__).parent
    print("\n🔧 Completing project setup...\n")
    
    # Models
    create_file(base / "datamatrix_decoder/core/models.py", """\"\"\"Data models for decoder results.\"\"\"

from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass
class DecodeResult:
    \"\"\"Result from barcode/Data Matrix decoding.\"\"\"
    
    data: str
    format: str
    rect: Optional[Tuple[int, int, int, int]] = None
    filename: Optional[str] = None
    
    def __str__(self) -> str:
        return f"{self.format.upper()}: {self.data}"
    
    def to_dict(self) -> dict:
        \"\"\"Convert to dictionary.\"\"\"
        return {
            "data": self.data,
            "format": self.format,
            "rect": self.rect,
            "filename": self.filename,
        }
""")
    
    # Decoder
    create_file(base / "datamatrix_decoder/core/decoder.py", """\"\"\"Core decoder implementation.\"\"\"

import logging
from pathlib import Path
from typing import List, Optional, Union
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    from pylibdmtx.pylibdmtx import decode as dmtx_decode
except ImportError:
    dmtx_decode = None

try:
    from pyzbar import pyzbar
except ImportError:
    pyzbar = None

from PIL import Image

from datamatrix_decoder.core.exceptions import DecodeError, UnsupportedFormatError
from datamatrix_decoder.core.models import DecodeResult


logger = logging.getLogger(__name__)


class DataMatrixDecoder:
    \"\"\"High-performance Data Matrix decoder.\"\"\"
    
    def __init__(self, timeout: int = 30):
        \"\"\"Initialize decoder.
        
        Args:
            timeout: Maximum time in seconds for decoding operation
        \"\"\"
        self.timeout = timeout
        if dmtx_decode is None:
            raise ImportError("pylibdmtx is required. Install: pip install pylibdmtx")
    
    def decode_image(self, image_path: Union[str, Path]) -> Optional[DecodeResult]:
        \"\"\"Decode Data Matrix from image file.
        
        Args:
            image_path: Path to image file
            
        Returns:
            DecodeResult if successful, None otherwise
        \"\"\"
        try:
            image = Image.open(image_path)
            decoded = dmtx_decode(image, timeout=self.timeout)
            
            if decoded:
                obj = decoded[0]
                return DecodeResult(
                    data=obj.data.decode("utf-8"),
                    format="datamatrix",
                    rect=obj.rect,
                    filename=str(image_path),
                )
            return None
        except Exception as e:
            logger.error(f"Error decoding {image_path}: {e}")
            raise DecodeError(f"Failed to decode image: {e}")
    
    def decode_batch(self, image_paths: List[Union[str, Path]], max_workers: int = 4) -> List[DecodeResult]:
        \"\"\"Decode multiple images in parallel.
        
        Args:
            image_paths: List of image file paths
            max_workers: Maximum number of parallel workers
            
        Returns:
            List of DecodeResult objects
        \"\"\"
        results = []
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(self.decode_image, path): path for path in image_paths}
            
            for future in as_completed(futures):
                try:
                    result = future.result()
                    if result:
                        results.append(result)
                except Exception as e:
                    logger.error(f"Batch decode error: {e}")
        
        return results


class BarcodeDecoder:
    \"\"\"Multi-format barcode decoder.\"\"\"
    
    SUPPORTED_FORMATS = [
        "datamatrix", "qrcode", "ean13", "ean8", "upca", "upce",
        "code128", "code39", "code93", "itf", "codabar", "pdf417", "aztec"
    ]
    
    def __init__(self, formats: Optional[List[str]] = None):
        \"\"\"Initialize barcode decoder.
        
        Args:
            formats: List of barcode formats to decode (None = all)
        \"\"\"
        if pyzbar is None:
            raise ImportError("pyzbar is required. Install: pip install pyzbar")
        
        self.formats = formats or self.SUPPORTED_FORMATS
        self._validate_formats()
    
    def _validate_formats(self):
        \"\"\"Validate requested formats are supported.\"\"\"
        for fmt in self.formats:
            if fmt not in self.SUPPORTED_FORMATS:
                raise UnsupportedFormatError(f"Format {fmt} not supported")
    
    def decode_image(self, image_path: Union[str, Path]) -> List[DecodeResult]:
        \"\"\"Decode all barcodes from image.
        
        Args:
            image_path: Path to image file
            
        Returns:
            List of DecodeResult objects
        \"\"\"
        try:
            image = Image.open(image_path)
            decoded = pyzbar.decode(image)
            
            results = []
            for obj in decoded:
                if obj.type.lower() in self.formats:
                    results.append(DecodeResult(
                        data=obj.data.decode("utf-8"),
                        format=obj.type.lower(),
                        rect=obj.rect,
                        filename=str(image_path),
                    ))
            
            return results
        except Exception as e:
            logger.error(f"Error decoding {image_path}: {e}")
            raise DecodeError(f"Failed to decode image: {e}")
    
    def decode_batch(self, image_paths: List[Union[str, Path]], max_workers: int = 4) -> List[DecodeResult]:
        \"\"\"Decode multiple images in parallel.\"\"\"
        results = []
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(self.decode_image, path): path for path in image_paths}
            
            for future in as_completed(futures):
                try:
                    batch_results = future.result()
                    results.extend(batch_results)
                except Exception as e:
                    logger.error(f"Batch decode error: {e}")
        
        return results
""")
    
    # CLI
    create_file(base / "datamatrix_decoder/cli/__init__.py", """\"\"\"CLI interface.\"\"\"
""")
    
    create_file(base / "datamatrix_decoder/cli/main.py", """\"\"\"Command-line interface.\"\"\"

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
    \"\"\"DataMatrix Decoder - Professional barcode decoding tool.\"\"\"
    pass


@cli.command()
@click.argument("image_path", type=click.Path(exists=True))
@click.option("--format", "-f", default="datamatrix", help="Barcode format")
def decode(image_path: str, format: str):
    \"\"\"Decode a single image.\"\"\"
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
    \"\"\"Batch process images.\"\"\"
    try:
        image_paths = list(Path(directory).glob("*.png")) + list(Path(directory).glob("*.jpg"))
        
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
            console.print(f"\\n[green]✓[/green] Saved to {output}")
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)


def main():
    cli()


if __name__ == "__main__":
    main()
""")
    
    create_file(base / "datamatrix_decoder/__main__.py", """\"\"\"Allow running as python -m datamatrix_decoder.\"\"\"

from datamatrix_decoder.cli.main import main

if __name__ == "__main__":
    main()
""")
    
    # Examples
    create_file(base / "examples/basic_usage.py", """\"\"\"Basic usage examples.\"\"\"

from datamatrix_decoder import DataMatrixDecoder, BarcodeDecoder

print("=" * 60)
print("DataMatrix Decoder - Usage Examples")
print("=" * 60)

print("\\n1. Data Matrix Decoder")
print("-" * 60)
print("decoder = DataMatrixDecoder()")
print("result = decoder.decode_image('path/to/datamatrix.png')")
print("if result:")
print("    print(f'Decoded: {result.data}')")

print("\\n2. Multi-format Barcode Decoder")
print("-" * 60)
print("barcode_decoder = BarcodeDecoder()")
print("results = barcode_decoder.decode_image('path/to/barcode.png')")
print("for result in results:")
print("    print(f'{result.format}: {result.data}')")

print("\\n3. Batch Processing")
print("-" * 60)
print("image_paths = ['image1.png', 'image2.png']")
print("results = barcode_decoder.decode_batch(image_paths, max_workers=4)")
print("for result in results:")
print("    print(f'{result.filename}: {result.data}')")

print("\\n" + "=" * 60)
print("✓ Examples ready! Add your image paths to test.")
print("=" * 60)
""")
    
    print("\n✅ All decoder files created successfully!")
    print("\n📋 Next steps:")
    print("1. Install dependencies: pip install -r requirements.txt")
    print("2. Test import: python -c \"from datamatrix_decoder import DataMatrixDecoder\"")
    print("3. Run examples: python examples/basic_usage.py")
    print("4. Use CLI: python -m datamatrix_decoder --help")


if __name__ == "__main__":
    main()