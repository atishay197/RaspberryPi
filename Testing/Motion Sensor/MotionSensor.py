import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
PIR_PIN = 26
GPIO.setup(PIR_PIN, GPIO.IN)

try:
               print "PIR Module Test (CTRL+C to exit)"
               time.sleep(2)
               print "Ready"
               while True:
                             if GPIO.input(PIR_PIN):
				print "Motion Detected!"
				time.sleep(7)
except KeyboardInterrupt:
               print "\nQuitting"
               GPIO.cleanup()
