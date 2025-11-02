from datamatrix_decoder import DataMatrixDecoder, BarcodeDecoder

print('=== DataMatrix Decoder Demo ===\n')

# Initialize decoders
dm_decoder = DataMatrixDecoder(timeout=30)
print('✅ DataMatrixDecoder initialized')

barcode_decoder = BarcodeDecoder()
print('✅ BarcodeDecoder initialized')

print(f'\n📊 Supported formats: {len(barcode_decoder.SUPPORTED_FORMATS)}')
print(f'   Formats: {", ".join(barcode_decoder.SUPPORTED_FORMATS[:5])}...')

print('\n✨ Decoder is ready to decode images!')
print('   Usage: decoder.decode_image("path/to/image.png")')
