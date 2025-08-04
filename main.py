#!/usr/bin/env python3
"""
DataMatrix Decoder - Project Generator

Run this script to generate the complete professional project structure.
"""

import os
from pathlib import Path


def create_file(path, content):
    """Create a file with content, creating parent directories if needed."""
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content, encoding='utf-8')
    print(f"✓ Created: {file_path.relative_to(Path.cwd())}")


def generate_project():
    """Generate complete DataMatrix Decoder project structure."""
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
PIPFILE.lock

# Testing / coverage
htmlcov/
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.pytest_cache/

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
*~

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
    
    # ==================== CORE MODULE ====================
    
    create_file(base / "datamatrix_decoder/__init__.py", """\"\"\"DataMatrix Decoder - Professional barcode decoding library.\"\"\"

__version__ = "1.0.0"
__author__ = "Leandre"

from datamatrix_decoder.core.decoder import DataMatrixDecoder, BarcodeDecoder
from datamatrix_decoder.core.exceptions import (
    DecoderError,
    ImageLoadError,
    DecodeError,
    UnsupportedFormatError,
)

__all__ = [
    "DataMatrixDecoder",
    "BarcodeDecoder",
    "DecoderError",
    "ImageLoadError",
    "DecodeError",
    "UnsupportedFormatError",
]
""")
    
    create_file(base / "datamatrix_decoder/core/__init__.py", """\"\"\"Core decoder functionality.\"\"\"

from datamatrix_decoder.core.decoder import DataMatrixDecoder, BarcodeDecoder
from datamatrix_decoder.core.exceptions import DecoderError

__all__ = ["DataMatrixDecoder", "BarcodeDecoder", "DecoderError"]
""")
    
    create_file(base / "datamatrix_decoder/core/exceptions.py", """\"\"\"Custom exceptions for the decoder.\"\"\"


class DecoderError(Exception):
    \"\"\"Base exception for decoder errors.\"\"\" 
    pass


class ImageLoadError(DecoderError):
    \"\"\"Raised when image cannot be loaded.\"\"\" 
    pass


class DecodeError(DecoderError):
    \"\"\"Raised when decoding fails.\"\"\" 
    pass


class UnsupportedFormatError(DecoderError):
    \"\"\"Raised when barcode format is not supported.\"\"\" 
    pass


class ConfigurationError(DecoderError):
    \"\"\"Raised when configuration is invalid.\"\"\" 
    pass
""")
    
    print("\n📦 Generating core modules...")
    

if __name__ == "__main__":
    generate_project()