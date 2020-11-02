
from micropython import const
from time import sleep_ms
import ustruct

# Display resolution
EPD_WIDTH  = const(200)
EPD_HEIGHT = const(200)
img1 = bytes([ 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X3C, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X3F, 0X80, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X3F, 0XE0, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X3F, 0XF8, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X0F, 0XFF, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X01, 0XFF, 0XC0, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X3F, 0XF8,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X0F, 0XFC, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X07,
0XFF, 0XFF, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X3F, 0XFF, 0XFF, 0X80, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X3F, 0XFF, 0XFF, 0X80, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X3F, 0XF0, 0X07, 0X80, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X3F, 0X00, 0X07, 0X80, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X00, 0X07, 0X80,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X01, 0X80, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X0F, 0XFC, 0X40, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X1F, 0XFF, 0XC0, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X3F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0X80, 0X00, 0X3F, 0XFF, 0XC0, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X80, 0X00, 0X3F, 0XFF, 0XC0, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X80, 0X00, 0X3D, 0XFF, 0XC0, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X20, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X80, 0X00, 0X38, 0XC7, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X80, 0X00, 0X38, 0XE3, 0X80, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X20, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X80, 0X00, 0X3C,
0XE1, 0XC0, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X80, 0X00, 0X3E, 0XF3, 0XC0, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X80,
0X00, 0X1E, 0XFF, 0XC0, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X80, 0X00, 0X1E, 0X7F, 0XC0, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X80, 0X00, 0X06, 0X7F, 0XC0, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X20, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X80, 0X00, 0X00, 0X3F, 0X80, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X80, 0X00, 0X00, 0X02, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X20, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X80, 0X3E, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X80, 0X3F, 0XFF, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X20, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X80, 0X3F,
0XFF, 0XFC, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X00, 0X00,
0X1F, 0XFF, 0XFF, 0XFF, 0XFF, 0XF8, 0X00, 0X80, 0X3F, 0XFF, 0XFF, 0XC0, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X00, 0X00, 0X1F, 0XFF, 0XFF, 0XFF, 0XFF, 0XF8, 0X00,
0X80, 0X1F, 0XFF, 0XFF, 0XC0, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20,
0X00, 0X00, 0X1F, 0XFF, 0XFF, 0XFF, 0XFF, 0XF8, 0X00, 0X80, 0X00, 0X7F, 0XFF, 0XC0, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X00, 0X00, 0X1F, 0XFF, 0XFF, 0XFF, 0XFF,
0XF8, 0X00, 0X80, 0X00, 0X00, 0X3F, 0XC0, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X20, 0X00, 0X00, 0X1F, 0XFF, 0XFF, 0XFF, 0XFF, 0XF8, 0X00, 0X80, 0X00, 0X00, 0X00, 0XC0,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X00, 0X00, 0X1F, 0XFF, 0XFF,
0XFF, 0XFF, 0XF8, 0X00, 0X80, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X20, 0X00, 0X00, 0X1F, 0XFF, 0XFF, 0XFF, 0XFF, 0XF8, 0X00, 0X80, 0X00, 0X07,
0XF0, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X00, 0X00, 0X1F,
0XFF, 0XFF, 0XFF, 0XFF, 0XF8, 0X00, 0X80, 0X00, 0X1F, 0XFE, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X00, 0X00, 0X1F, 0XFF, 0XFF, 0XFF, 0XFF, 0XF8, 0X00, 0X80,
0X00, 0X3F, 0XFF, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X00,
0X00, 0X1F, 0XFF, 0XFF, 0XFF, 0XFF, 0XF8, 0X00, 0X80, 0X00, 0X3F, 0XFF, 0X80, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X00, 0X00, 0X1F, 0XF8, 0X00, 0X00, 0X1F, 0XF8,
0X00, 0X80, 0X00, 0X3F, 0XFF, 0XC0, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X20, 0X00, 0X00, 0X1F, 0XF8, 0X00, 0X00, 0X1F, 0XF8, 0X00, 0X80, 0X00, 0X3E, 0X0F, 0XC0, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X00, 0X00, 0X1F, 0XF8, 0X00, 0X00,
0X1F, 0XF8, 0X00, 0X80, 0X00, 0X3E, 0X07, 0XC0, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X20, 0X00, 0X00, 0X1F, 0XF8, 0X00, 0X00, 0X1F, 0XF8, 0X00, 0X80, 0X00, 0X1E, 0X03,
0XC0, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X00, 0X00, 0X1F, 0XF8,
0X00, 0X00, 0X1F, 0XF8, 0X00, 0X80, 0X00, 0X0E, 0X03, 0XC0, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X20, 0X00, 0X00, 0X1F, 0XF8, 0X00, 0X00, 0X1F, 0XF8, 0X00, 0X80, 0X00,
0X3F, 0X87, 0XC0, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X00, 0X00,
0X1F, 0XF8, 0X00, 0X00, 0X1F, 0XF8, 0X00, 0X80, 0X00, 0X3F, 0XFF, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X00, 0X00, 0X1F, 0XF8, 0X00, 0X00, 0X1F, 0XF8, 0X00,
0X80, 0X00, 0X3F, 0XFF, 0XFC, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20,
0X00, 0X00, 0X1F, 0XF8, 0X00, 0X00, 0X1F, 0XF8, 0X00, 0X80, 0X00, 0X3F, 0XFF, 0XFF, 0X80, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X00, 0X00, 0X1F, 0XF8, 0X00, 0X00, 0X1F,
0XF8, 0X00, 0X80, 0X00, 0X3F, 0XFF, 0XFF, 0X80, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X20, 0X00, 0X00, 0X1F, 0XF8, 0X00, 0X00, 0X1F, 0XF8, 0X00, 0X80, 0X00, 0X00, 0X3F, 0XFF,
0X80, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X00, 0X00, 0X1F, 0XF8, 0X00,
0X00, 0X1F, 0XF8, 0X00, 0X80, 0X00, 0X00, 0X00, 0XFF, 0X80, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X20, 0X00, 0X00, 0X1F, 0XF8, 0X00, 0X00, 0X1F, 0XF8, 0X00, 0X80, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X00, 0X00, 0X1F,
0XF8, 0X00, 0X00, 0X1F, 0XF8, 0X00, 0X80, 0X00, 0X0E, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X00, 0X00, 0X1F, 0XF8, 0X00, 0X00, 0X1F, 0XF8, 0X00, 0X80,
0X00, 0X1E, 0X3E, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X00,
0X00, 0X1F, 0XF8, 0X00, 0X00, 0X1F, 0XF8, 0X00, 0X80, 0X00, 0X3E, 0X7F, 0X80, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X00, 0X00, 0X1F, 0XF8, 0X00, 0X00, 0X1F, 0XF8,
0X00, 0X80, 0X00, 0X3E, 0XFF, 0X80, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X20, 0X00, 0X00, 0X1F, 0XF8, 0X00, 0X00, 0X1F, 0XF8, 0X00, 0X80, 0X00, 0X38, 0XFF, 0XC0, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X00, 0X00, 0X1F, 0XF8, 0X00, 0X00,
0X1F, 0XF8, 0X00, 0X80, 0X00, 0X38, 0XFF, 0XC0, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X20, 0X00, 0X00, 0X1F, 0XF8, 0X00, 0X00, 0X1F, 0XF8, 0X00, 0X80, 0X00, 0X39, 0XF1,
0XC0, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X00, 0X00, 0X1F, 0XF8,
0X00, 0X00, 0X00, 0X00, 0X00, 0X80, 0X00, 0X3F, 0XF1, 0XC0, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X20, 0X03, 0XFE, 0X00, 0X00, 0X1F, 0XF8, 0X00, 0X00, 0X00, 0X80, 0X00,
0X1F, 0XF1, 0XC0, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X03, 0XFE,
0X00, 0X00, 0X1F, 0XF8, 0X00, 0X00, 0X00, 0X80, 0X00, 0X1F, 0XF7, 0XC0, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X03, 0XFE, 0X00, 0X00, 0X1F, 0XF8, 0X00, 0X00, 0X00,
0X80, 0X00, 0X0F, 0XE7, 0XC0, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20,
0X03, 0XFE, 0X00, 0X00, 0X1F, 0XF8, 0X00, 0X00, 0X00, 0X80, 0X00, 0X07, 0XC7, 0X80, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X03, 0XFE, 0X00, 0X00, 0X1F, 0XF8, 0X00,
0X00, 0X00, 0X80, 0X00, 0X00, 0X07, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X20, 0X03, 0XFE, 0X00, 0X00, 0X1F, 0XF8, 0X00, 0X00, 0X00, 0X80, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X03, 0XFE, 0X00, 0X00, 0X1F,
0XF8, 0X00, 0X00, 0X00, 0X80, 0X3E, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X20, 0X03, 0XFE, 0X00, 0X00, 0X1F, 0XF8, 0X00, 0X00, 0X00, 0X80, 0X3E, 0X3F,
0XC0, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X03, 0XFE, 0X00,
0X00, 0X1F, 0XF8, 0X00, 0X00, 0X00, 0X80, 0X3E, 0X3F, 0XFF, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X03, 0XFE, 0X00, 0X00, 0X1F, 0XF8, 0X1F, 0XF8, 0X00, 0X80,
0X3E, 0X3F, 0XFF, 0XC0, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X03,
0XFE, 0X00, 0X00, 0X1F, 0XF8, 0X1F, 0XF8, 0X00, 0X80, 0X0E, 0X3F, 0XFF, 0XC0, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X03, 0XFE, 0X00, 0X00, 0X1F, 0XF8, 0X1F, 0XF8,
0X00, 0X80, 0X00, 0X0F, 0XFF, 0XC0, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X20, 0X03, 0XFE, 0X00, 0X00, 0X1F, 0XF8, 0X1F, 0XF8, 0X00, 0X80, 0X00, 0X00, 0X1F, 0XC0, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X20, 0X03, 0XFE, 0X00, 0X00, 0X1F, 0XF8,
0X1F, 0XF8, 0X00, 0X80, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,
0X00, 0X00, 0X20, 0X03, 0XFE, 0X00, 0X00, 0X1F, 0XF8, 0X1F, 0XF8, 0X00, 0X80, 0X00, 0X00, 0X00,
0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XDF, 0XFC, 0X01, 0XFF, 0XFF,
0XE0, 0X07, 0XE0, 0X07, 0XFF, 0X7F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XDF, 0XFC, 0X01, 0XFF, 0XFF, 0XE0, 0X07, 0XE0, 0X07, 0XFF, 0X7F, 0XFF,
0X00, 0X1F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XDF, 0XFC, 0X01,
0XFF, 0XFF, 0XE0, 0X07, 0XE0, 0X07, 0XFF, 0X7F, 0XFC, 0X00, 0X07, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XDF, 0XFC, 0X01, 0XFF, 0XFF, 0XE0, 0X07, 0XE0, 0X07, 0XFF,
0X7F, 0XF8, 0X00, 0X03, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XDF,
0XFC, 0X01, 0XFF, 0XFF, 0XE0, 0X07, 0XE0, 0X07, 0XFF, 0X7F, 0XF0, 0X00, 0X01, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XDF, 0XFC, 0X00, 0X00, 0X00, 0X00, 0X07, 0XE0,
0X07, 0XFF, 0X7F, 0XF0, 0X7F, 0XC0, 0X7F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XDF, 0XFC, 0X00, 0X00, 0X00, 0X00, 0X07, 0XE0, 0X07, 0XFF, 0X7F, 0XF0, 0XE0, 0X60, 0X3F,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XDF, 0XFC, 0X00, 0X00, 0X00, 0X00,
0X07, 0XE0, 0X07, 0XFF, 0X7F, 0XF0, 0X80, 0X10, 0X3F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XDF, 0XFC, 0X00, 0X00, 0X00, 0X00, 0X07, 0XE0, 0X07, 0XFF, 0X7F, 0XF0, 0X8F,
0X08, 0X3F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XDF, 0XFC, 0X00, 0X00,
0X00, 0X00, 0X07, 0XE0, 0X07, 0XFF, 0X7F, 0XF0, 0X9F, 0XC4, 0X3F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XDF, 0XFC, 0X00, 0X00, 0X00, 0X00, 0X07, 0XE0, 0X07, 0XFF, 0X7F,
0XF0, 0X9F, 0XE4, 0X3F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XDF, 0XFC,
0X00, 0X00, 0X00, 0X00, 0X07, 0XE0, 0X07, 0XFF, 0X7F, 0XF0, 0X9F, 0XE4, 0X3F, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XDF, 0XFC, 0X00, 0X00, 0X00, 0X00, 0X07, 0XE0, 0X07,
0XFF, 0X7F, 0XF0, 0X9F, 0XE4, 0X3F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XDF, 0XFC, 0X00, 0X00, 0X00, 0X00, 0X07, 0XE0, 0X07, 0XFF, 0X7F, 0XF0, 0X07, 0XE4, 0X3F, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XDF, 0XFC, 0X00, 0X00, 0X00, 0X00, 0X07,
0XE0, 0X07, 0XFF, 0X7F, 0XF0, 0X00, 0XE4, 0X3F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XDF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XE0, 0X07, 0XFF, 0X7F, 0XF0, 0X00, 0X04,
0X3F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XDF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XE0, 0X07, 0XFF, 0X7F, 0XF0, 0X00, 0X00, 0X3F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XDF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XE0, 0X07, 0XFF, 0X7F, 0XFF,
0X80, 0X00, 0X3F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XDF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XE0, 0X07, 0XFF, 0X7F, 0XFF, 0XFC, 0X00, 0X3F, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XDF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XE0, 0X07, 0XFF,
0X7F, 0XFF, 0XFF, 0XE0, 0X3F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XDF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XE0, 0X07, 0XFF, 0X7F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XDF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XE0,
0X07, 0XFF, 0X7F, 0XFF, 0XFE, 0X1F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XDF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XE0, 0X07, 0XFF, 0X7F, 0XFF, 0XF8, 0X03, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XDF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XE0, 0X07, 0XFF, 0X7F, 0XFF, 0XF0, 0X00, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XDF, 0XFF, 0XFF, 0XE0, 0X00, 0X00, 0X00, 0X00, 0X07, 0XFF, 0X7F, 0XFF, 0XE0,
0X00, 0X7F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XDF, 0XFF, 0XFF, 0XE0,
0X00, 0X00, 0X00, 0X00, 0X07, 0XFF, 0X7F, 0XFF, 0XE0, 0X00, 0X7F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XDF, 0XFF, 0XFF, 0XE0, 0X00, 0X00, 0X00, 0X00, 0X07, 0XFF, 0X7F,
0XFF, 0XE1, 0XF8, 0X3F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XDF, 0XFF,
0XFF, 0XE0, 0X00, 0X00, 0X00, 0X00, 0X07, 0XFF, 0X7F, 0XFF, 0XE3, 0XFE, 0X3F, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XDF, 0XFF, 0XFF, 0XE0, 0X00, 0X00, 0X00, 0X00, 0X07,
0XFF, 0X7F, 0XFF, 0XE3, 0XFF, 0X1F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XDF, 0XFF, 0XFF, 0XE0, 0X00, 0X00, 0X00, 0X00, 0X07, 0XFF, 0X7F, 0XFF, 0XE3, 0XFF, 0X1F, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XDF, 0XFF, 0XFF, 0XE0, 0X00, 0X00, 0X00,
0X00, 0X07, 0XFF, 0X7F, 0XFF, 0XE1, 0XFF, 0X1F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XDF, 0XFF, 0XFF, 0XE0, 0X00, 0X00, 0X00, 0X00, 0X07, 0XFF, 0X7F, 0XFF, 0XE0, 0XFF,
0X1F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XDF, 0XFF, 0XFF, 0XE0, 0X00,
0X00, 0X00, 0X00, 0X07, 0XFF, 0X7F, 0XFF, 0XF0, 0X7E, 0X1F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XDF, 0XFF, 0XFF, 0XE0, 0X00, 0X00, 0X00, 0X00, 0X07, 0XFF, 0X7F, 0XFF,
0XF0, 0X00, 0X1F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XDF, 0XFF, 0XFF,
0XE0, 0X00, 0X00, 0X00, 0X00, 0X07, 0XFF, 0X7F, 0XFF, 0XF8, 0X00, 0X3F, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XDF, 0XFF, 0XFF, 0XE0, 0X00, 0X00, 0X00, 0X00, 0X07, 0XFF,
0X7F, 0XFF, 0XFE, 0X00, 0X3F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XDF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0X7F, 0XFF, 0XFF, 0X00, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XDF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0X7F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XDF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0X7F, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XDF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0X7F, 0XFF, 0XFC, 0X0F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XDF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0X7F, 0XFF, 0XF8,
0X01, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XDF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0X7F, 0XFF, 0XF0, 0X00, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XDF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0X7F,
0XFF, 0XE0, 0X00, 0X7F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XDF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0X7F, 0XFF, 0XE0, 0XE0, 0X3F, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XDF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0X7F, 0XFF, 0XE3, 0XFC, 0X3F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XDF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0X7F, 0XFF, 0XE3, 0XFE, 0X1F, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XDF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0X7F, 0XFF, 0XE3, 0XFF, 0X1F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XDF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0X7F, 0XFF, 0XE3, 0XFF,
0X1F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XDF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0X7F, 0XFF, 0XE1, 0XFF, 0X1F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XDF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0X7F, 0XFF,
0XE0, 0XFE, 0X1F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XDF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0X7F, 0XFF, 0XF0, 0X1C, 0X1F, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XDF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0X7F, 0XFF, 0XF8, 0X00, 0X1F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XDF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0X7F, 0XFF, 0XFC, 0X00, 0X3F, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XDF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0X7F, 0XFF, 0XFE, 0X00, 0X7F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XC0, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X7F, 0XFF, 0XFF, 0X80, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0X1E, 0X7F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFE, 0X1E, 0X07, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFC, 0X1E, 0X00, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XF8, 0X0E, 0X00, 0X7F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XF8, 0X3E, 0X00, 0X7F, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XF8, 0X7E, 0X20, 0X3F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XF8, 0X7E, 0X3C,
0X3F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XF8, 0XFE, 0X3E, 0X3F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XF8,
0XFE, 0X3E, 0X1F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XF8, 0XFE, 0X3E, 0X1F, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XF8, 0X7F, 0XFF, 0X1F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XF8, 0X7F, 0XFF, 0X1F, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XF8, 0X7F, 0XFF, 0X1F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFC, 0X3F, 0XFE, 0X1F,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFC, 0X1F, 0XFE, 0X1F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFE, 0X07,
0XFC, 0X3F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0X00, 0X60, 0X3F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0X80, 0X00, 0X3F, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XC0, 0X00, 0X7F, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XF8, 0X00, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFE, 0X07, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,])

# Display commands
DRIVER_OUTPUT_CONTROL                = const(0x01)
BOOSTER_SOFT_START_CONTROL           = const(0x0C)
DEEP_SLEEP_MODE                      = const(0x10)
DATA_ENTRY_MODE_SETTING              = const(0x11)
MASTER_ACTIVATION                    = const(0x20)
DISPLAY_UPDATE_CONTROL_2             = const(0x22)
WRITE_RAM                            = const(0x24)
WRITE_VCOM_REGISTER                  = const(0x2C)
WRITE_LUT_REGISTER                   = const(0x32)
SET_DUMMY_LINE_PERIOD                = const(0x3A)
SET_GATE_TIME                        = const(0x3B) # not in datasheet
SET_RAM_X_ADDRESS_START_END_POSITION = const(0x44)
SET_RAM_Y_ADDRESS_START_END_POSITION = const(0x45)
SET_RAM_X_ADDRESS_COUNTER            = const(0x4E)
SET_RAM_Y_ADDRESS_COUNTER            = const(0x4F)
TERMINATE_FRAME_READ_WRITE           = const(0xFF) # aka NOOP

BUSY = const(1)  # 1=busy, 0=idle


class EPD:
    def __init__(self, spi, cs, dc, rst, busy):
        self.spi = spi
        self.cs = cs
        self.dc = dc
        self.rst = rst
        self.busy = busy
        self.cs.value(0)
        self.dc.value(0)
        self.rst.value(1)
        self.width = EPD_WIDTH
        self.height = EPD_HEIGHT

    lut_vcom0 = bytearray(b'\x0E\x14\x01\x0A\x06\x04\x0A\x0A\x0F\x03\x03\x0C\x06\x0A\x00')
    lut_w = bytearray(b'\x0E\x14\x01\x0A\x46\x04\x8A\x4A\x0F\x83\x43\x0C\x86\x0A\x04')
    lut_b = bytearray(b'\x0E\x14\x01\x8A\x06\x04\x8A\x4A\x0F\x83\x43\x0C\x06\x4A\x04')
    lut_g1 = bytearray(b'\x8E\x94\x01\x8A\x06\x04\x8A\x4A\x0F\x83\x43\x0C\x06\x0A\x04')
    lut_g2 = bytearray(b'\x8E\x94\x01\x8A\x06\x04\x8A\x4A\x0F\x83\x43\x0C\x06\x0A\x04')
    lut_vcom1 = bytearray(b'\x03\x1D\x01\x01\x08\x23\x37\x37\x01\x00\x00\x00\x00\x00\x00')
    lut_red0 = bytearray(b'\x83\x5D\x01\x81\x48\x23\x77\x77\x01\x00\x00\x00\x00\x00\x00')
    lut_red1 = bytearray(b'\x03\x1D\x01\x01\x08\x23\x37\x37\x01\x00\x00\x00\x00\x00\x00')

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
        self._data(0x07) # 设置高低电压
        self._data(0x00)
        self._data(0x0B) # 红色电压设置，值越大红色越深
        self._data(0x00)
        self._command(0x06)
        self._data(0x07)
        self._data(0x07)
        self._data(0x07)
        self._command(0x04) # 上电

        if self.wait_until_idle() == False:
            pass

        self._command(0X00)
        self._data(0xcf) # 选择最大分辨率

        self._command(0X50)
        self._data(0x37)

        self._command(0x30)
        self._data(0x39) # PLL设定

        self._command(0x61)  # 像素设定
        self._data(0xC8) # 200像素
        self._data(0x00) # 200像素
        self._data(0xC8)

        self._command(0x82) # vcom设定
        self._data(0x18)

        self.lut_bw()
        self.lut_red()

    def wait_until_idle(self):
        for i in range(10):
            sleep_ms(100)
            if self.busy.value() != BUSY:
                return True;
        print('self.busy', self.busy.value())
        return False;

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

    # put an image in the frame memory
    def set_frame_memory(self, image, x, y, w, h):
        # x point must be the multiple of 8 or the last 3 bits will be ignored
        x = x & 0xF8
        w = w & 0xF8

        if (x + w >= self.width):
            x_end = self.width - 1
        else:
            x_end = x + w - 1

        if (y + h >= self.height):
            y_end = self.height - 1
        else:
            y_end = y + h - 1

        self.set_memory_area(x, y, x_end, y_end)
        self.set_memory_pointer(x, y)
        self._command(WRITE_RAM, image)

    # replace the frame memory with the specified color
    def clear_frame_memory(self, color):
        self.set_memory_area(0, 0, self.width - 1, self.height - 1)
        self.set_memory_pointer(0, 0)
        self._command(WRITE_RAM)
        # send the color data
        for i in range(0, self.width, 8 * self.height):
            self._data(bytearray([color]))

    # draw the current frame memory and switch to the next memory area
    def display_frame(self):
        self._command(DISPLAY_UPDATE_CONTROL_2, b'\xC4')
        self._command(MASTER_ACTIVATION)
        self._command(TERMINATE_FRAME_READ_WRITE)
        self.wait_until_idle()

    # specify the memory area for data R/W
    def set_memory_area(self, x_start, y_start, x_end, y_end):
        self._command(SET_RAM_X_ADDRESS_START_END_POSITION)
        # x point must be the multiple of 8 or the last 3 bits will be ignored
        self._data(bytearray([(x_start >> 3) & 0xFF]))
        self._data(bytearray([(x_end >> 3) & 0xFF]))
        self._command(SET_RAM_Y_ADDRESS_START_END_POSITION, ustruct.pack("<HH", y_start, y_end))

    # specify the start point for data R/W
    def set_memory_pointer(self, x, y):
        self._command(SET_RAM_X_ADDRESS_COUNTER)
        # x point must be the multiple of 8 or the last 3 bits will be ignored
        self._data(bytearray([(x >> 3) & 0xFF]))
        self._command(SET_RAM_Y_ADDRESS_COUNTER, ustruct.pack("<H", y))
        self.wait_until_idle()

    # to wake call reset() or init()
    def sleep(self):
        self._command(DEEP_SLEEP_MODE, b'\x01') # enter deep sleep A0=1, A0=0 power on
        self.wait_until_idle()

if __name__ == "__main__":
    import utime
    from Maix import GPIO
    from board import board_info
    from fpioa_manager import fm

    from machine import SPI

    # #  SPMOD Interface
    # #  # [4|5] [7  |VCC] [RST|3V3]
    # #  # [3|6] [15 | 21] [D/C|SCK]
    # #  # [2|7] [20 |  8] [CS |SI ]
    # #  # [1|8] [GND|  6] [GND|BL ]

    # #define SPI_IPS_LCD_CS_PIN_NUM 20
    # #define SPI_IPS_LCD_SCK_PIN_NUM 21
    # #define SPI_IPS_LCD_MOSI_PIN_NUM 8
    spi1 = SPI(SPI.SPI1, mode=SPI.MODE_MASTER, baudrate=600 * 1000,
            polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=21, mosi=8)

    fm.register(20, fm.fpioa.GPIOHS20, force=True) # #define SPI_IPS_LCD_SS_PIN_NUM 20
    fm.register(15, fm.fpioa.GPIOHS15, force=True) # #define SPI_IPS_LCD_DC_PIN_NUM 15
    fm.register(6, fm.fpioa.GPIOHS6, force=True) # #define SPI_IPS_LCD_BUSY_PIN_NUM 6
    fm.register(7, fm.fpioa.GPIOHS7, force=True) # #define SPI_IPS_LCD_RST_PIN_NUM 7

    cs = GPIO(GPIO.GPIOHS20, GPIO.OUT)
    dc = GPIO(GPIO.GPIOHS15, GPIO.OUT)
    busy = GPIO(GPIO.GPIOHS6, GPIO.IN, GPIO.PULL_DOWN)
    rst = GPIO(GPIO.GPIOHS7, GPIO.OUT)

    tmp = EPD(spi1, cs, dc, rst, busy)

    tmp.init()


    print('test')
