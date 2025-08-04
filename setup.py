from setuptools import setup, find_packages

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
