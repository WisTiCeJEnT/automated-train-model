#include <avr/io.h>
#include "peri.h"

void init_peri()
{
    // PB0..PB5 -> output
    DDRB |= (1<<PB2)|(1<<PB1)|(1<<PB0)|(1<<PB5)|(1<<PB4)|(1<<PB3);

    // PC0..PC3 -> input
    DDRC &= ~((1<<PC2)|(1<<PC1)|(1<<PC0)|(1<<PC3));

    // enable pull-up resistor on PC3
    //PORTC |= (1<<PC3);

    // turn off all LEDs
    set_led_value(0);
}

void set_led_value(uint8_t value)
{
    PORTB &= ~(0b111111);
    PORTB |= (value & 0b111);    //green light
    PORTB |= ((~value & 0b111)<<3);   //red light
}

uint16_t read_adc(uint8_t channel)
{
    ADMUX = (0<<REFS1)|(1<<REFS0) // use VCC as reference voltage
          | (0<<ADLAR)            // store result to the right of ADCH/ADCL
          | (channel & 0b1111);   // point MUX to the specified channel
 
    ADCSRA = (1<<ADEN)            // enable ADC
           | (1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0) // set speed to 1/128 of system clock
           | (1<<ADSC);           // start conversion
 
    // wait until ADSC bit becomes 0, indicating complete conversion
    while ((ADCSRA & (1<<ADSC)))
       ;
 
    return ADCL + ADCH*256;
}
