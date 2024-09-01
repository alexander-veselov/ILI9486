import time
from ili9486.ili9486 import ILI9486
from spidev import SpiDev
from utils import create_gradient_image, create_text_image

def get_driver(angle=90, mirrored=False):
    spi = SpiDev(0, 0)
    spi.mode = 0b10
    spi.max_speed_hz = 48000000
    return ILI9486(dc=24, rst=25, spi=spi, angle=angle, mirrored=mirrored)

def test_rotations():
    for angle in [0, 90, 180, 270]:
        for mirrored in [False, True]:
            driver = get_driver(angle, mirrored)
            image = create_text_image(driver.get_size(), driver.get_angle(), driver.get_mirorred())
            driver.display(image)
            time.sleep(3)
            driver.reset()

def test_fps():
    driver = get_driver()
    image = create_gradient_image(driver.get_size())
    frames = 0
    fps_data = []
    frame_start_time = time.time()
    while len(fps_data) < 10:
        driver.display(image)
        frames += 1
        current_time = time.time()
        elapsed_time = current_time - frame_start_time
        if elapsed_time >= 1.0:
            fps = frames / elapsed_time
            fps_data.append(fps)
            frame_start_time = current_time
            frames = 0
    driver.reset()
    print("Min FPS:", min(fps_data))
    print("Average FPS:", sum(fps_data) / len(fps_data))

def main():
    test_fps()
    test_rotations()

if __name__ == '__main__':
    main()