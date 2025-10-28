"""DataMatrix Decoder - Professional barcode decoding library."""

__version__ = "1.0.0"
__author__ = "Leandre"

from datamatrix_decoder.core.decoder import DataMatrixDecoder, BarcodeDecoder
from datamatrix_decoder.core.exceptions import (
    DecoderError,
    ImageLoadError,
    DecodeError,
    UnsupportedFormatError,
    ConfigurationError,
)
from datamatrix_decoder.core.models import DecodeResult

__all__ = [
    "DataMatrixDecoder",
    "BarcodeDecoder",
    "DecodeResult",
    "DecoderError",
    "ImageLoadError",
    "DecodeError",
    "UnsupportedFormatError",
    "ConfigurationError",
]

# Clean, simple imports following KISS principle

