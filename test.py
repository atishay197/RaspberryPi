#!/usr/bin/env python

import max7219.led as led
device = led.matrix(cascaded=1)
device.show_message("HELLO WORLD")
