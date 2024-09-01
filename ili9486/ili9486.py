import time
import itertools
import RPi.GPIO as GPIO
from PIL import Image
from spidev import SpiDev

class ILI9486:
    def __init__(self, spi: SpiDev, dc: int, rst: int, angle: int = 90, mirrored: bool = False):
        self.spi = spi
        self.dc = dc
        self.rst = rst
        self.size = (320, 480)
        self.angle = angle
        self.mirrored = mirrored
        self.origin = {
            (0,   False): 0x48,
            (0,   True ): 0x08,
            (90,  False): 0xE8,
            (90,  True ): 0x68,
            (180, False): 0x88,
            (180, True ): 0xC8,
            (270, False): 0x28,
            (270, True ): 0xA8,
        }[(angle, mirrored)]

        if self.angle == 90 or self.angle == 270:
            self.size = self.size[1], self.size[0]

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.dc, GPIO.OUT)
        GPIO.output(self.dc, GPIO.HIGH)
        GPIO.setup(self.rst, GPIO.OUT)
        GPIO.output(self.rst, GPIO.HIGH)

        self.reset()

        self.command(0xF1); self.data([0x36, 0x04, 0x00, 0x3C, 0x0F, 0x8F], size=1)
        self.command(0xF2); self.data([0x18, 0xA3, 0x12, 0x02, 0xB2, 0x12, 0xFF, 0x10, 0x00], size=1)
        self.command(0xF8); self.data([0x21, 0x04], size=1)
        self.command(0xF9); self.data([0x00, 0x08], size=1)
        self.command(0x36); self.data([0x08], size=1)
        self.command(0xB4); self.data([0x00], size=1)
        self.command(0xC1); self.data([0x41], size=1)
        self.command(0xC5); self.data([0x00, 0x91, 0x80, 0x00], size=1)
        self.command(0xE0); self.data([0x0F, 0x1F, 0x1C, 0x0C, 0x0F, 0x08, 0x48, 0x98, 0x37, 0x0A, 0x13, 0x04, 0x11, 0x0D, 0x00], size=1)
        self.command(0xE1); self.data([0x0F, 0x32, 0x2E, 0x0B, 0x0D, 0x05, 0x47, 0x75, 0x37, 0x06, 0x10, 0x03, 0x24, 0x20, 0x00], size=1)
        self.command(0x3A); self.data([0x66], size=1)
        self.command(0x11)
        self.command(0x36); self.data([self.origin], size=1)
        self.command(0xFF)
        self.command(0x29)
        self.command(0x2A); self.data([0, 0, self.size[0] >> 8, self.size[0] & 0xFF], size=1)
        self.command(0x2B); self.data([0, 0, self.size[1] >> 8, self.size[1] & 0xFF], size=1)

    def data(self, data, size=4096):
        GPIO.output(self.dc, GPIO.HIGH)
        for start in range(0, len(data), size):
            end = min(start + size, len(data))
            self.spi.writebytes(data[start:end])

    def command(self, data):
        GPIO.output(self.dc, GPIO.LOW)
        self.spi.writebytes([data])

    def reset(self):
        GPIO.output(self.rst, GPIO.HIGH)
        time.sleep(.02)
        GPIO.output(self.rst, GPIO.LOW)
        time.sleep(.02)
        GPIO.output(self.rst, GPIO.HIGH)
        time.sleep(.120)

    def display(self, image: Image):
        if image.size != self.size:
            raise Exception("Image size doesn't match screen size")
        self.command(0x2C)
        self.data(list(itertools.chain.from_iterable(image.getdata())))

    def get_size(self):
        return self.size

    def get_mirorred(self):
        return self.mirrored

    def get_angle(self):
        return self.angle