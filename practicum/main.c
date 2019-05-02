#include <avr/io.h>
#include <avr/interrupt.h>  /* for sei() */
#include <util/delay.h>     /* for _delay_ms() */
#include <avr/pgmspace.h>   /* required by usbdrv.h */

#include "peri.h"
#include "usbdrv.h"

#define RQ_SET_SIGNAL_LIGHT   0
#define RQ_GET_LIGHT       1

/* ------------------------------------------------------------------------- */
/* ----------------------------- USB interface ----------------------------- */
/* ------------------------------------------------------------------------- */
usbMsgLen_t usbFunctionSetup(uint8_t data[8])
{
    usbRequest_t *rq = (void *)data;

    /* declared as static so they stay valid when usbFunctionSetup returns */
    static uint8_t state;  
    static uint16_t ls[4];  

    if (rq->bRequest == RQ_SET_SIGNAL_LIGHT)
    {
        uint8_t led_state = rq->wValue.bytes[0];
        set_led_value(led_state);
        return 0;
    }

    else if (rq->bRequest == RQ_GET_LIGHT)
    {
        ls[0] = read_adc(PC0);
        ls[1] = read_adc(PC1);
        ls[2] = read_adc(PC2);
        ls[3] = read_adc(PC3);
        usbMsgPtr = &ls;

        return 8;
    }


    /* default for not implemented requests: return no data back to host */
    return 0;
}

/* ------------------------------------------------------------------------- */
int main(void)
{
    init_peri();

    usbInit();

    /* enforce re-enumeration, do this while interrupts are disabled! */
    usbDeviceDisconnect();
    _delay_ms(300);
    usbDeviceConnect();

    /* enable global interrupts */
    sei();

    /* main event loop */
    for(;;)
    {
        usbPoll();
    }

    return 0;
}

/* ------------------------------------------------------------------------- */
