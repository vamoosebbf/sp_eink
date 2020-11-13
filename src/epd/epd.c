#include "board_config.h"
#include "Ap_29demo.h"
#include "epd.h"
#include "fpioa.h"
#include "gpiohs.h"
#include "sleep.h"
#include "spi.h"

#define DATALENGTH 8

void EPD_io_mux_init(void)
{
    fpioa_set_function(SPI_EINK_CS_PIN_NUM, FUNC_SPI1_SS0);   // CS
    fpioa_set_function(SPI_EINK_SCK_PIN_NUM, FUNC_SPI1_SCLK); // SCLK
    fpioa_set_function(SPI_EINK_MOSI_PIN_NUM, FUNC_SPI1_D0);  // MOSI

    fpioa_set_function(SPI_EINK_DC_PIN_NUM, FUNC_GPIOHS0 + SPI_EINK_DC_GPIO_NUM);   // D2
    fpioa_set_function(SPI_EINK_RST_PIN_NUM, FUNC_GPIOHS0 + SPI_EINK_RST_GPIO_NUM); // D3
    fpioa_set_function(SPI_EINK_BL_PIN_NUM, FUNC_GPIOHS0 + SPI_EINK_BL_GPIO_NUM);   // D2

    gpiohs_set_drive_mode(SPI_EINK_DC_GPIO_NUM, GPIO_DM_OUTPUT);
    gpiohs_set_drive_mode(SPI_EINK_RST_GPIO_NUM, GPIO_DM_OUTPUT);

    gpiohs_set_pin(SPI_EINK_DC_GPIO_NUM, GPIO_PV_HIGH);
    gpiohs_set_pin(SPI_EINK_RST_GPIO_NUM, GPIO_PV_HIGH);

    gpiohs_set_drive_mode(SPI_EINK_BL_PIN_NUM, GPIO_DM_INPUT_PULL_UP);
    gpiohs_set_pin_edge(SPI_EINK_BL_PIN_NUM, GPIO_PE_BOTH);
}

static void spi_write_reg(uint8_t reg_addr, uint8_t data)
{
    uint8_t cmd[2] = {reg_addr, data};

    spi_init(SPI_INDEX, SPI_WORK_MODE_0, SPI_FF_STANDARD, DATALENGTH, 0);
    spi_send_data_standard(SPI_INDEX, SPI_CHIP_SELECT_NSS, cmd, 2, NULL, 0);
}

static void spi_read_reg(uint8_t reg_addr, uint8_t *reg_data)
{
    uint8_t cmd[1] = {reg_addr};

    spi_init(SPI_INDEX, SPI_WORK_MODE_0, SPI_FF_STANDARD, DATALENGTH, 0);
    spi_receive_data_standard(SPI_INDEX, SPI_CHIP_SELECT_NSS, cmd, 1, reg_data, 1);
}

static void EPD_W21_WriteCMD(uint8_t command)
{
    uint8_t cmd[1] = {command};
    gpiohs_set_pin(SPI_EINK_DC_GPIO_NUM, GPIO_PV_LOW);

    spi_init(SPI_INDEX, SPI_WORK_MODE_0, SPI_FF_STANDARD, DATALENGTH, 0);
    spi_send_data_standard(SPI_INDEX, SPI_CHIP_SELECT_NSS, cmd, 1, NULL, 0);

    gpiohs_set_pin(SPI_EINK_DC_GPIO_NUM, GPIO_PV_HIGH);
}

static void EPD_W21_WriteDATA(uint8_t data)
{
    uint8_t cmd[1] = {data};
    gpiohs_set_pin(SPI_EINK_DC_GPIO_NUM, GPIO_PV_HIGH);

    spi_init(SPI_INDEX, SPI_WORK_MODE_0, SPI_FF_STANDARD, DATALENGTH, 0);
    spi_send_data_standard(SPI_INDEX, SPI_CHIP_SELECT_NSS, cmd, 1, NULL, 0);
}

uint8_t k = 1;
void lut_bw(void)
{
    unsigned int count;
    EPD_W21_WriteCMD(0x20);
    for (count = 0; count < 15; count++)
    {
        EPD_W21_WriteDATA(lut_vcom0[count]);
    }

    EPD_W21_WriteCMD(0x21);
    for (count = 0; count < 15; count++)
    {
        EPD_W21_WriteDATA(lut_w[count]);
    }

    EPD_W21_WriteCMD(0x22);
    for (count = 0; count < 15; count++)
    {
        EPD_W21_WriteDATA(lut_b[count]);
    }

    EPD_W21_WriteCMD(0x23);
    for (count = 0; count < 15; count++)
    {
        EPD_W21_WriteDATA(lut_g1[count]);
    }

    EPD_W21_WriteCMD(0x24);
    for (count = 0; count < 15; count++)
    {
        EPD_W21_WriteDATA(lut_g2[count]);
    }
}

void lut_red(void)
{
    unsigned int count;
    EPD_W21_WriteCMD(0x25);
    for (count = 0; count < 15; count++)
    {
        EPD_W21_WriteDATA(lut_vcom1[count]);
    }

    EPD_W21_WriteCMD(0x26);
    for (count = 0; count < 15; count++)
    {
        EPD_W21_WriteDATA(lut_red0[count]);
    }

    EPD_W21_WriteCMD(0x27);
    for (count = 0; count < 15; count++)
    {
        EPD_W21_WriteDATA(lut_red1[count]);
    }
}

void EPD_CheckStatus(void)
{
    while (!gpiohs_get_pin(SPI_EINK_BL_GPIO_NUM))
        ;
}

void EPD_DisplayInit(void)
{
    EPD_io_mux_init();

    gpiohs_set_pin(SPI_EINK_RST_GPIO_NUM, GPIO_PV_LOW);
    msleep(100);
    gpiohs_set_pin(SPI_EINK_RST_GPIO_NUM, GPIO_PV_HIGH);
    msleep(100);

    gpiohs_set_pin(SPI_EINK_BL_GPIO_NUM, GPIO_PV_LOW);
    msleep(100);

    EPD_W21_WriteCMD(0x01);
    EPD_W21_WriteDATA(0x07); //设置高低电压
    EPD_W21_WriteDATA(0x00);
    EPD_W21_WriteDATA(0x0B); //红色电压设置，值越大红色越深
    EPD_W21_WriteDATA(0x00);

    EPD_W21_WriteCMD(0x06); //boost设定
    EPD_W21_WriteDATA(0x07);
    EPD_W21_WriteDATA(0x07);
    EPD_W21_WriteDATA(0x07);

    EPD_W21_WriteCMD(0x04); //上电
    EPD_CheckStatus();      //查看芯片状态

    EPD_W21_WriteCMD(0X00);
    EPD_W21_WriteDATA(0xcf); //选择最大分辨率

    EPD_W21_WriteCMD(0X50);
    EPD_W21_WriteDATA(0x37);

    EPD_W21_WriteCMD(0x30); //PLL设定
    EPD_W21_WriteDATA(0x39);

    EPD_W21_WriteCMD(0x61);  //像素设定
    EPD_W21_WriteDATA(0xC8); //200像素
    EPD_W21_WriteDATA(0x00); //200像素
    EPD_W21_WriteDATA(0xC8);

    EPD_W21_WriteCMD(0x82); //vcom设定
    EPD_W21_WriteDATA(0x18);

    lut_bw();
    lut_red();
}

/////////////////////////////Enter deep sleep mode////////////////////////
void EPD_Sleep(void) //Enter deep sleep mode
{
    EPD_W21_WriteCMD(0X50);  //VCOM AND DATA INTERVAL SETTING
    EPD_W21_WriteDATA(0xf7); //WBmode:VBDF 17|D7 VBDW 97 VBDB 57		WBRmode:VBDF F7 VBDW 77 VBDB 37  VBDR B7

    EPD_W21_WriteCMD(0X02); //power off
    EPD_CheckStatus();      //waiting for the electronic paper IC to release the idle signal
    EPD_W21_WriteCMD(0X07); //deep sleep
    EPD_W21_WriteDATA(0xA5);
}

/***************************full display function*************************************/
void EPD_FullDisplayClearing(void) //Clear the screen for the first time
{
    unsigned int i, j;

    for (j = 0; j < 2; j++)
    {
        EPD_W21_WriteCMD(0x10);
        for (i = 0; i < 5000; i++)
        {
            EPD_W21_WriteDATA(0x00);
        }
        msleep(2);
        EPD_W21_WriteCMD(0x13);
        for (i = 0; i < 5000; i++)
        {
            EPD_W21_WriteDATA(0xff);
        }
        msleep(2);

        EPD_W21_WriteCMD(0x04); //Power on
        msleep(100);
        EPD_CheckStatus();
        EPD_W21_WriteCMD(0x12); //DISPLAY REFRESH
        msleep(100);            //!!!The delay here is necessary, 200uS at least!!!
        EPD_CheckStatus();
    }
}

void EPD_FullDisplay(const unsigned char *old_data, const unsigned char *new_data, unsigned char mode) // mode0:Refresh picture1,mode1:Refresh picture2... ,mode2:Clear
{
    unsigned int i;

    if (mode == 0) //mode0:Refresh picture1
    {
        EPD_W21_WriteCMD(0x10);
        for (i = 0; i < 10000; i++)
        {
            EPD_W21_WriteDATA(0xff);
        }
        msleep(2);
        EPD_W21_WriteCMD(0x13);
        for (i = 0; i < 5000; i++)
        {
            EPD_W21_WriteDATA(new_data[i]);
        }
        msleep(2);
    }

    else if (mode == 1) //mode0:Refresh picture2...
    {
        EPD_W21_WriteCMD(0x10);
        for (i = 0; i < 5000; i++)
        {
            EPD_W21_WriteDATA(old_data[i]);
        }
        msleep(2);
        EPD_W21_WriteCMD(0x13);
        for (i = 0; i < 5000; i++)
        {
            EPD_W21_WriteDATA(new_data[i]);
        }
        msleep(2);
    }

    else
    {
        EPD_W21_WriteCMD(0x10);
        for (i = 0; i < 5000; i++)
        {
            EPD_W21_WriteDATA(old_data[i]);
        }
        msleep(2);
        EPD_W21_WriteCMD(0x13);
        for (i = 0; i < 5000; i++)
        {
            EPD_W21_WriteDATA(0xff);
        }
        msleep(2);
    }

    EPD_W21_WriteCMD(0x04); //Power on
    msleep(100);
    EPD_CheckStatus();

    EPD_W21_WriteCMD(0x12); //DISPLAY REFRESH
    msleep(100);            //!!!The delay here is necessary, 200uS at least!!!
    EPD_CheckStatus();
}
