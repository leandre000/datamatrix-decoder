"""DataMatrix Decoder - Professional barcode decoding library."""

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
