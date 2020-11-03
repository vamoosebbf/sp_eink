/* Copyright 2018 Canaan Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
#include <bsp.h>
#include <stdio.h>
#include <sysctl.h>
#include "board_config.h"
#include "syslog.h"

#include "epd/demo.h"
#include "epd/epd.h"
#include "fpioa.h"
#include "gpiohs.h"
#include "uarths.h"
#include "gui/gui_paint.h"

unsigned char BlackImage[5000]; //Define canvas space

void epd_test(void)
{

    EPD_DisplayInit(); //EPD init

    //Paint initialization
    Paint_NewImage(BlackImage, EPD_WIDTH, EPD_HEIGHT, 270, WHITE); //Set screen size and display orientation

    Paint_Clear(WHITE);
    //Point
    Paint_DrawPoint(5, 10, BLACK, DOT_PIXEL_1X1, DOT_STYLE_DFT);
    Paint_DrawPoint(5, 25, BLACK, DOT_PIXEL_2X2, DOT_STYLE_DFT);
    Paint_DrawPoint(5, 40, BLACK, DOT_PIXEL_3X3, DOT_STYLE_DFT);
    Paint_DrawPoint(5, 55, BLACK, DOT_PIXEL_4X4, DOT_STYLE_DFT);
    //Line
    Paint_DrawLine(20, 10, 70, 60, BLACK, LINE_STYLE_SOLID, DOT_PIXEL_1X1);
    Paint_DrawLine(70, 10, 20, 60, BLACK, LINE_STYLE_SOLID, DOT_PIXEL_1X1);
    //Rectangle
    Paint_DrawRectangle(20, 10, 70, 60, BLACK, DRAW_FILL_EMPTY, DOT_PIXEL_1X1);
    Paint_DrawRectangle(85, 10, 130, 60, BLACK, DRAW_FILL_FULL, DOT_PIXEL_1X1);
    //Circle
    Paint_DrawCircle(30, 120, 25, BLACK, DRAW_FILL_EMPTY, DOT_PIXEL_1X1);
    Paint_DrawCircle(100, 120, 25, BLACK, DRAW_FILL_FULL, DOT_PIXEL_1X1);
    EPD_FullDisplay(BlackImage, BlackImage, 0);

    Paint_Clear(WHITE);
    Paint_DrawString_EN(0, 0, "sipeed", &Font8, WHITE, BLACK);   //5*8
    Paint_DrawString_EN(0, 10, "sipeed", &Font12, WHITE, BLACK); //7*12
    Paint_DrawString_EN(0, 25, "sipeed", &Font16, WHITE, BLACK); //11*16
    Paint_DrawString_EN(0, 45, "sipeed", &Font20, WHITE, BLACK); //14*20
    Paint_DrawString_EN(0, 80, "sipeed", &Font24, WHITE, BLACK); //17*24
    EPD_FullDisplay(BlackImage, BlackImage, 0);                  //display image

    Paint_Clear(WHITE);
    Paint_DrawNum(0, 0, 123456789, &Font8, WHITE, BLACK);   //5*8
    Paint_DrawNum(0, 10, 123456789, &Font12, WHITE, BLACK); //7*12
    Paint_DrawNum(0, 25, 123456789, &Font16, WHITE, BLACK); //11*16
    Paint_DrawNum(0, 45, 123456789, &Font20, WHITE, BLACK); //14*20
    Paint_DrawNum(0, 70, 123456789, &Font24, WHITE, BLACK); //17*24
    EPD_FullDisplay(BlackImage, BlackImage, 0);

    EPD_Sleep(); //epd_sleep,Sleep instruction is necessary, please do not delete!!!
}

int main(void)
{
    uint32_t freq = 0;
    freq = sysctl_pll_set_freq(SYSCTL_PLL0, 800000000);
    uint64_t core = current_coreid();
    printk(LOG_COLOR_W "-------------------------------\r\n");
    printk(LOG_COLOR_W "Sipeed\r\n");
    printk(LOG_COLOR_W "Compile@ %s %s\r\n", __DATE__, __TIME__);
    printk(LOG_COLOR_W "Board: " LOG_COLOR_E BOARD_NAME "\r\n");
    printk(LOG_COLOR_W "pll freq: %dhz\r\n", freq);
    printk(LOG_COLOR_W "-------------------------------\r\n");

    epd_test();

    printk(LOG_COLOR_W "-------------END---------------\r\n");
    while (1)
        ;
    return 0;
}
