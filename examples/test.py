import time
from ili9486.ili9486 import ILI9486
from spidev import SpiDev
from utils import create_gradient_image, create_text_image

def get_driver(angle=90, mirrored=False):
    spi = SpiDev(0, 0)
    spi.mode = 0b10
    spi.max_speed_hz = 48000000
    return ILI9486(dc=24, rst=25, spi=spi, angle=angle, mirrored=mirrored)

def test_gradient():
    driver = get_driver()
    image = create_gradient_image(driver.get_size())
    driver.display(image)
    time.sleep(10)
    driver.reset()

def test_rotations():
    for angle in [0, 90, 180, 270]:
        for mirrored in [False, True]:
            driver = get_driver(angle, mirrored)
            image = create_text_image(driver.get_size(), driver.get_angle(), driver.get_mirorred())
            driver.display(image)
            time.sleep(3)
            driver.reset()

def main():
    test_gradient()
    test_rotations()

if __name__ == '__main__':
    main()