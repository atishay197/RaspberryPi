#!/usr/bin/env python

import max7219.led as led
import time
from max7219.font import proportional, CP437_FONT, SINCLAIR_FONT, LCD_FONT , UKR_FONT
device = led.matrix(cascaded=1)

def heart():
    device.pixel(1,1,1,redraw=True)
    device.pixel(2,1,1,redraw=True)
    device.pixel(5,1,1,redraw=True)
    device.pixel(6,1,1,redraw=True)
    
    device.pixel(0,2,1,redraw=True)
    device.pixel(7,2,1,redraw=True)
    device.pixel(3,2,1,redraw=True)
    device.pixel(4,2,1,redraw=True)
    device.pixel(0,3,1,redraw=True)
    device.pixel(7,3,1,redraw=True)
    
    device.pixel(1,4,1,redraw=True)
    device.pixel(6,4,1,redraw=True)
    device.pixel(2,5,1,redraw=True)
    device.pixel(5,5,1,redraw=True)
    device.pixel(3,6,1,redraw=True)
    device.pixel(4,6,1,redraw=True)

device.orientation(90)

heart()
time.sleep(100)
device.clear()
