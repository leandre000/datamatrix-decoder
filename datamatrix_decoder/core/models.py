"""Data models for decoder results."""

from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass
class DecodeResult:
    """Result from barcode/Data Matrix decoding."""
    
    data: str
    format: str
    rect: Optional[Tuple[int, int, int, int]] = None
    filename: Optional[str] = None
    
    def __str__(self) -> str:
        return f"{self.format.upper()}: {self.data}"
    
    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            "data": self.data,
            "format": self.format,
            "rect": self.rect,
            "filename": self.filename,
        }
