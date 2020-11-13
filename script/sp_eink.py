from micropython import const
from time import sleep_ms
import ustruct
import image

# Display resolution
EPD_WIDTH = const(200)
EPD_HEIGHT = const(200)
BUSY = const(1)  # 1=busy, 0=idle


class EPD:
    def __init__(self, spi, cs, dc, rst, busy, width, height):
        self.spi = spi
        self.cs = cs
        self.dc = dc
        self.rst = rst
        self.busy = busy
        self.cs.value(0)
        self.dc.value(0)
        self.rst.value(1)
        self.width = width
        self.height = height

    lut_vcom0 = bytearray(
        b'\x0E\x14\x01\x0A\x06\x04\x0A\x0A\x0F\x03\x03\x0C\x06\x0A\x00')
    lut_w = bytearray(
        b'\x0E\x14\x01\x0A\x46\x04\x8A\x4A\x0F\x83\x43\x0C\x86\x0A\x04')
    lut_b = bytearray(
        b'\x0E\x14\x01\x8A\x06\x04\x8A\x4A\x0F\x83\x43\x0C\x06\x4A\x04')
    lut_g1 = bytearray(
        b'\x8E\x94\x01\x8A\x06\x04\x8A\x4A\x0F\x83\x43\x0C\x06\x0A\x04')
    lut_g2 = bytearray(
        b'\x8E\x94\x01\x8A\x06\x04\x8A\x4A\x0F\x83\x43\x0C\x06\x0A\x04')
    lut_vcom1 = bytearray(
        b'\x03\x1D\x01\x01\x08\x23\x37\x37\x01\x00\x00\x00\x00\x00\x00')
    lut_red0 = bytearray(
        b'\x83\x5D\x01\x81\x48\x23\x77\x77\x01\x00\x00\x00\x00\x00\x00')
    lut_red1 = bytearray(
        b'\x03\x1D\x01\x01\x08\x23\x37\x37\x01\x00\x00\x00\x00\x00\x00')

    def _command(self, command, data=None):
        self.dc(0)
        self.cs(0)
        self.spi.write(bytearray([command]))
        self.cs(1)
        if data is not None:
            self._data(data)
        self.dc(1)

    def _data(self, data):
        self.dc(1)
        self.cs(0)
        self.spi.write(data)
        self.cs(1)

    def reset(self):
        self.dc(0)
        sleep_ms(200)
        self.dc(1)
        self.rst(0)
        sleep_ms(100)
        self.rst(1)
        sleep_ms(200)

    def init(self):
        self.reset()
        self._command(0x01)
        self._data(0x07)  # 设置高低电压
        self._data(0x00)
        self._data(0x0B)  # 红色电压设置，值越大红色越深
        self._data(0x00)
        self._command(0x06)
        self._data(0x07)
        self._data(0x07)
        self._data(0x07)
        self._command(0x04)  # 上电

        if self.wait_until_idle() == False:
            pass

        self._command(0X00)
        self._data(0xcf)  # 选择最大分辨率

        self._command(0X50)
        self._data(0x37)

        self._command(0x30)
        self._data(0x39)  # PLL设定

        self._command(0x61)  # 像素设定
        self._data(0xC8)  # 200像素
        self._data(0x00)  # 200像素
        self._data(0xC8)

        self._command(0x82)  # vcom设定
        self._data(0x18)

        self.lut_bw()
        self.lut_red()

    def display(self, img):
        self._command(0x10)  # write "B/W" data to SRAM. 0x00:black
        for i in range(10000):
            self._data(0xff)

        img1 = image.Image()  # handle image
        img1 = img1.resize(self.width, self.height)
        img1.draw_image(img, 0, 0)
        # Parameter 'fov' is to slove data loss issues
        img1.rotation_corr(x_rotation=180, fov=2)
        img_bytes = img1.to_bytes()  # That's "self.width*self.height*2" bytes

        self._command(0x13)  # write "RED" data to SRAM 0x00:red,0xff:white
        for i in range(0, self.width*self.height*2, 16):
            b = 0
            for j in range(0, 15, 2):
                if img_bytes[i+j] or img_bytes[i+j+1]:
                    b = b | (0x80 >> j//2)
            self._data(~b)

        self._command(0x12)  # display refresh
        self.wait_until_idle()

    def wait_until_idle(self):
        for i in range(10):
            sleep_ms(100)
            if self.busy.value() != BUSY:
                return True
        print('self.busy', self.busy.value())
        return False

    def set_lut(self, lut):
        self._command(WRITE_LUT_REGISTER, lut)

    def lut_bw(self):
        self._command(0x20, EPD.lut_vcom0)
        self._command(0x21, EPD.lut_w)
        self._command(0x22, EPD.lut_b)
        self._command(0x23, EPD.lut_g1)
        self._command(0x24, EPD.lut_g2)

    def lut_red(self):
        self._command(0x25, EPD.lut_vcom1)
        self._command(0x26, EPD.lut_red0)
        self._command(0x27, EPD.lut_red1)

    # enter deep sleep A0=1, A0=0 power on
    def sleep(self):
        self._command(0x50)
        self._data(0xf7)

        self._command(0x02)
        self.wait_until_idle()
        self._data(0x07)
        self._command(0xa5)


if __name__ == "__main__":
    import utime
    from Maix import GPIO
    from board import board_info
    from fpioa_manager import fm

    from machine import SPI
    import lcd

    # #  SPMOD Interface
    # #  # [4|5] [7  |VCC] [RST|3V3]
    # #  # [3|6] [15 | 21] [D/C|SCK]
    # #  # [2|7] [20 |  8] [CS |SI ]
    # #  # [1|8] [GND|  6] [GND|BL ]

    # #define SPI_EINK_CS_PIN_NUM 20
    # #define SPI_EINK_SCK_PIN_NUM 21
    # #define SPI_EINK_MOSI_PIN_NUM 8
    spi1 = SPI(SPI.SPI1, mode=SPI.MODE_MASTER, baudrate=600 * 1000,
               polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=21, mosi=8)

    # define SPI_EINK_SS_PIN_NUM 20
    fm.register(20, fm.fpioa.GPIOHS20, force=True)
    # define SPI_EINK_DC_PIN_NUM 15
    fm.register(15, fm.fpioa.GPIOHS15, force=True)
    # define SPI_EINK_BUSY_PIN_NUM 6
    fm.register(6, fm.fpioa.GPIOHS6, force=True)
    # define SPI_EINK_RST_PIN_NUM 7
    fm.register(7, fm.fpioa.GPIOHS7, force=True)

    cs = GPIO(GPIO.GPIOHS20, GPIO.OUT)
    dc = GPIO(GPIO.GPIOHS15, GPIO.OUT)
    busy = GPIO(GPIO.GPIOHS6, GPIO.IN, GPIO.PULL_DOWN)
    rst = GPIO(GPIO.GPIOHS7, GPIO.OUT)

    lcd.init()
    epd = EPD(spi1, cs, dc, rst, busy, EPD_WIDTH, EPD_HEIGHT)
    epd.init()

    img = image.Image()
    img = img.resize(200, 200)
    img.draw_line(0, 0, 100, 100)
    img.draw_circle(50, 50, 20)
    img.draw_rectangle(80, 80, 30, 30)

    epd.display(img)
    epd.sleep()
    lcd.display(img)
