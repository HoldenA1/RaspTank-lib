## RaspTank Library
A library that allows you to use python to easily interface with the adeept RaspTank

### Setup
Required software:
- [Python3](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/installing/)

Install libraries:
```
$ pip install rpi_ws281x Adafruit_PCA9685
```

Setup I2C Servo Motors:
- `nano /boot/config.txt`
- Add dtparam=i2c1=on
- ctrl-x, y, enter
- reboot

### Documentation
For further instructions and documentation, please visit the [GitBook](https://holden-adamec.gitbook.io/adeept-python-library/).
