#ifndef __epd_H__
#define __epd_H__
#include "syslog.h"

#define EPD_WIDTH   200
#define EPD_HEIGHT  200

void EPD_DisplayInit(void);
void EPD_FullDisplay(const unsigned char *old_data, const unsigned char *new_data, unsigned char mode); // mode0:Refresh picture1,mode1:Refresh picture2... ,mode2:Clear
void EPD_FullDisplay_clearing(void);
void EPD_Sleep(void);
#endif
