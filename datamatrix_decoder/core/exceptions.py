"""Custom exceptions for the decoder."""


class DecoderError(Exception):
    """Base exception for decoder errors.""" 
    pass


class ImageLoadError(DecoderError):
    """Raised when image cannot be loaded.""" 
    pass


class DecodeError(DecoderError):
    """Raised when decoding fails.""" 
    pass


class UnsupportedFormatError(DecoderError):
    """Raised when barcode format is not supported.""" 
    pass


class ConfigurationError(DecoderError):
    """Raised when configuration is invalid.""" 
    pass
