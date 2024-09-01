import time
from PIL import Image
from spidev import SpiDev
from ili9486.ili9486 import ILI9486

def generate_gradient(size):
    gradient_image = Image.new('RGB', size)
    width, height = size
    for x in range(width):
        for y in range(height):
            normalized_x = x / width
            normalized_y = y / height
            r = int(normalized_x * 255)
            g = int(normalized_y * 255)
            b = int((1 - normalized_x) * 255)
            gradient_image.putpixel((x, y), (r, g, b))
    return gradient_image

def main():
    spi = SpiDev(0, 0)
    spi.mode = 0b10
    spi.max_speed_hz = 48000000
    driver = ILI9486(dc=24, rst=25, spi=spi)

    image = generate_gradient(driver.get_size())
    driver.display(image)
    time.sleep(10)
    driver.reset()

if __name__ == '__main__':
    main()