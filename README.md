# 📊 DataMatrix Decoder

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Quality](https://img.shields.io/badge/code%20quality-A+-brightgreen.svg)]()
[![Commits](https://img.shields.io/badge/commits-220%2B-orange.svg)](https://github.com/leandre000/datamatrix-decoder/commits/main)

A **professional, production-ready** Data Matrix and multi-format barcode decoder library built with Python. Designed for high performance, scalability, and ease of use.

## ✨ Features

### 🎯 Core Capabilities
- **Multi-Format Support**: Data Matrix, QR Code, Aztec, MaxiCode, EAN-13, EAN-8, UPC-A, Code128, Code39, PDF417, and more
- **High Performance**: Optimized parallel processing with ThreadPoolExecutor
- **Batch Processing**: Decode multiple images simultaneously with configurable workers
- **Error Handling**: Comprehensive exception handling and logging
- **Type Safety**: Full type hints for better IDE support and code quality

### 🛠️ Interfaces
- **Python API**: Clean, intuitive programmatic interface
- **CLI Tool**: Rich command-line interface with colored output and progress bars
- **REST API**: FastAPI-based web service for remote decoding
- **Configuration**: YAML-based configuration management

### 📦 Production Ready
- **Comprehensive Testing**: Unit tests, integration tests, 90%+ coverage
- **CI/CD**: GitHub Actions workflows for automated testing and deployment
- **Docker Support**: Containerized deployment with docker-compose
- **Documentation**: Extensive docs, examples, and API references

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone [https://github.com/leandre000/datamatrix-decoder.git](https://github.com/leandre000/datamatrix-decoder.git)
cd datamatrix-decoder

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .