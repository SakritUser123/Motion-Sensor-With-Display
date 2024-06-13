
import i2c_driver
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

pirPIN = 17
GPIO.setup(pirPIN,GPIO.IN)
mylcd = i2c_driver.LCD()


while True:
pir_val = GPIO.input(pirPIN)
if pir_val == GPIO.HIGH:
mylcd.lcd_display_string('HEllo',1)
time.sleep(3)
lcd_clear(self)
