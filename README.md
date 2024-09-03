# ILI9486

[![last-commit](https://img.shields.io/github/last-commit/alexander-veselov/ILI9486)](https://github.com/alexander-veselov/ILI9486/commits/master/)

ILI9486 Python driver for Raspberry Pi.

This module is intended for integration into other applications and is not suitable for use as a driver for desktop visualization. It supports displaying images only and does not include touchscreen functionality.

# Install
```bash
# Enable SPI
# Interface Options > SPI > Yes > Ok > Finish 
sudo raspi-config

# Clone a repository
git clone https://github.com/alexander-veselov/ILI9486.git

# Create Python virtual environment
python3 -m venv venv

# Activate Python virtual environment
source ./venv/bin/activate

# Install required dependencies
pip3 install .
```

# Usage
You can find usage example here: [test.py](https://github.com/alexander-veselov/ILI9486/blob/main/examples/test.py)
```bash
# Make sure SPI is enabled and venv is activated
python3 ./examples/test.py
```
If the screen does not work, try changing the following ```SpiDev``` settings: ```max_speed_hz``` and ```mode```

# Hardware
- Tested on Raspberry Pi 5 only
- Display: 3.5 inch RPi LCD Display

# Performance
- ```test_fps``` shows ```5 FPS``` (see [test.py](https://github.com/alexander-veselov/ILI9486/blob/main/examples/test.py))
- Performance could definitely be better, but I haven't found any way to improve it yet

# Photos
Note: In real life, the display has nice, rich colors without any artifacts. Artifacts present in photographs are camera distortions
<p align="center">
    <img width="49%" src="https://github.com/user-attachments/assets/316f455d-30e8-41d5-b90e-f619add96abc"/>
&nbsp;
    <img width="49%" src="https://github.com/user-attachments/assets/683332b0-6f5f-4070-857f-8e86944bb2d5"/>
</p>

<p align="center">
    <img width="49%" src="https://github.com/user-attachments/assets/ebead24e-e265-424a-9add-7ed729a4ee00"/>
&nbsp;
    <img width="49%" src="https://github.com/user-attachments/assets/70c85cc1-c04f-453a-97d9-d54cb5f2e5e9"/>
</p>
