#!/usr/bin/env python3
"""
DataMatrix Decoder - Complete Project Generator
Run this script to generate all project files and directories.
"""

from pathlib import Path


def create_file(path, content):
    """Create file with content, making parent directories as needed."""
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content, encoding='utf-8')
    print(f"✓ Created: {file_path.relative_to(Path.cwd())}")


def generate_project():
    """Generate complete project structure."""
    base = Path(__file__).parent
    
    print("\n🚀 Generating DataMatrix Decoder Project...\n")
    
    # ==================== ROOT FILES ====================
    
    create_file(base / ".gitignore", """# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
.env
.venv
env/
venv/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Project specific
config.local.yaml
test_images/
output/
*.png
*.jpg
*.jpeg
*.gif
*.bmp
""")
    
    create_file(base / "requirements.txt", """# Core dependencies
pylibdmtx==0.1.10
pyzbar==0.1.9
Pillow==10.1.0
opencv-python==4.8.1.78
numpy==1.24.3

# Web API
fastapi==0.104.1
uvicorn[standard]==0.24.0
python-multipart==0.0.6

# CLI
click==8.1.7
rich==13.7.0

# Configuration
PyYAML==6.0.1
python-dotenv==1.0.0

# Utilities
typing-extensions==4.8.0
pydantic==2.5.0

# Logging
coloredlogs==15.0.1
""")
    
    create_file(base / "requirements-dev.txt", """-r requirements.txt

# Testing
pytest==7.4.3
pytest-cov==4.1.0
pytest-asyncio==0.21.1

# Code quality
black==23.11.0
flake8==6.1.0
mypy==1.7.1
pylint==3.0.2
isort==5.12.0
""")
    
    create_file(base / "setup.py", """from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="datamatrix-decoder",
    version="1.0.0",
    author="Leandre",
    description="Professional Data Matrix and barcode decoder",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leandre000/datamatrix-decoder",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pylibdmtx>=0.1.10",
        "pyzbar>=0.1.9",
        "Pillow>=10.1.0",
        "opencv-python>=4.8.1",
        "numpy>=1.24.3",
        "fastapi>=0.104.1",
        "uvicorn>=0.24.0",
        "click>=8.1.7",
        "rich>=13.7.0",
        "PyYAML>=6.0.1",
        "pydantic>=2.5.0",
    ],
    entry_points={
        "console_scripts": [
            "datamatrix-decoder=datamatrix_decoder.cli.main:main",
        ],
    },
)
""")
    
    create_file(base / "config.yaml", """# DataMatrix Decoder Configuration

logging:
  level: INFO
  format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
  file: null

decoder:
  timeout: 30
  max_workers: 4
  formats:
    - datamatrix
    - qrcode
    - aztec
    - maxicode
    - ean13
    - ean8
    - upca
    - code128
    - code39
    - pdf417

api:
  host: 0.0.0.0
  port: 8000
  max_file_size: 10485760
  workers: 4
""")
    
    create_file(base / "LICENSE", """MIT License

Copyright (c) 2024 Leandre

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
""")
    
    # ==================== README ====================
    
    create_file(base / "README.md", """# 📊 DataMatrix Decoder

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
""")
    
    print("\n✅ Project generated successfully!")
    print("\n📋 Next steps:")
    print("1. Install dependencies: pip install -r requirements.txt")
    print("2. Run: python complete_setup.py (to add decoder files)")
    print("3. Test: python examples/basic_usage.py")


if __name__ == "__main__":
    generate_project()