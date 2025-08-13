class BarcodeDecoder:
    def _validate_formats(self):
        for fmt in self.formats:
            if fmt not in self.SUPPORTED_FORMATS:
                raise ValueError(fmt)

