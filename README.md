# 📊 DataMatrix Decoder

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A professional, production-ready Data Matrix and barcode decoder library with support for multiple formats, batch processing, CLI, and REST API.

## ✨ Features

- **Multiple Format Support**: Data Matrix, QR Code, Aztec, MaxiCode, EAN, UPC, Code128, and more
- **Batch Processing**: Process multiple images in parallel
- **CLI Interface**: Easy-to-use command-line tool
- **REST API**: FastAPI-based web service
- **High Performance**: Optimized for speed and accuracy
- **Comprehensive Logging**: Detailed logging with configurable levels
- **Type Hints**: Fully typed for better IDE support

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/leandre000/datamatrix-decoder.git
cd datamatrix-decoder

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

```python
from datamatrix_decoder import DataMatrixDecoder, BarcodeDecoder

# Decode Data Matrix
decoder = DataMatrixDecoder()
result = decoder.decode_image("path/to/image.png")
if result:
    print(f"Decoded: {result.data}")

# Decode multiple formats
barcode_decoder = BarcodeDecoder()
results = barcode_decoder.decode_image("path/to/barcode.png")
for result in results:
    print(f"{result.format}: {result.data}")
```

## 📖 Documentation

See examples in the `examples/` directory.

## 📝 License

MIT License - see LICENSE file for details.

---

**Made with ❤️ for the barcode community**
