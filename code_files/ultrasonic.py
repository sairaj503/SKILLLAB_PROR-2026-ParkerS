import RPi.GPIO as GPIO
from RPLCD.i2c import CharLCD
from time import sleep, time

# LCD setup
lcd = CharLCD('PCF8574', 0x27, port=1, cols=16, rows=2)

# Pins
TRIG = 17
ECHO = 27
GREEN_LED = 22
RED_LED = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

def get_distance():
    GPIO.output(TRIG, True)
    sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time()

    duration = pulse_end - pulse_start
    distance = round(duration * 17150, 2)
    return distance

def set_leds(distance):
    if distance <= 10:
        GPIO.output(RED_LED, True)
        GPIO.output(GREEN_LED, False)
    else:
        GPIO.output(GREEN_LED, True)
        GPIO.output(RED_LED, False)

# Startup message
lcd.write_string('Distance Meter')
sleep(2)
lcd.clear()

try:
    while True:
        dist = get_distance()
        set_leds(dist)

        lcd.home()
        lcd.write_string('Distance:       ')
        lcd.crlf()

        if dist <= 10:
            lcd.write_string(f'{dist} cm  CLOSE! ')
        else:
            lcd.write_string(f'{dist} cm  SAFE   ')

        print(f"Distance: {dist} cm | {'RED - Too Close' if dist <= 10 else 'GREEN - Safe'}")
        sleep(0.5)

except KeyboardInterrupt:
    lcd.clear()
    lcd.write_string('Goodbye!')
    sleep(1)
    lcd.close(clear=True)
    GPIO.output(RED_LED, False)
    GPIO.output(GREEN_LED, False)
    GPIO.cleanup()