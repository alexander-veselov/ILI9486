from setuptools import setup, find_packages

setup(
    name='ili9486',
    version='1.0.0',
    packages=find_packages(),
    install_requires=["Pillow", "RPi.GPIO", "rpi-lgpio", "spidev"],
    author='Oleksandr Veselov',
    description='ILI9486 Python driver for Raspberry Pi',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/alexander-veselov/ILI9486',
)