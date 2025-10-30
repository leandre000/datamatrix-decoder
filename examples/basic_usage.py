"""Basic usage examples."""

from datamatrix_decoder import DataMatrixDecoder, BarcodeDecoder

print("=" * 60)
print("DataMatrix Decoder - Usage Examples")
print("=" * 60)

print("\n1. Data Matrix Decoder")
print("-" * 60)
print("decoder = DataMatrixDecoder()")
print("result = decoder.decode_image('path/to/datamatrix.png')")
print("if result:")
print("    print(f'Decoded: {result.data}')")

print("\n2. Multi-format Barcode Decoder")
print("-" * 60)
print("barcode_decoder = BarcodeDecoder()")
print("results = barcode_decoder.decode_image('path/to/barcode.png')")
print("for result in results:")
print("    print(f'{result.format}: {result.data}')")

print("\n3. Batch Processing")
print("-" * 60)
print("image_paths = ['image1.png', 'image2.png']")
print("results = barcode_decoder.decode_batch(image_paths, max_workers=4)")
print("for result in results:")
print("    print(f'{result.filename}: {result.data}')")

print("\n" + "=" * 60)
print("✓ Examples ready! Add your image paths to test.")
print("=" * 60)

# Clear, concise examples

