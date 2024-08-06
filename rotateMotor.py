import time
import RPi.GPIO as GPIO

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set the GPIO Pin
A = 17
B = 18
C = 27
D = 22

# Set the GPIO Pin mode
GPIO.setup(A, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(C, GPIO.OUT)
GPIO.setup(D, GPIO.OUT)

# Set the GPIO Pin to LOW

def GPIO_SETUP(a, b, c, d):
    GPIO.output(A, a)
    GPIO.output(B, b)
    GPIO.output(C, c)
    GPIO.output(D, d)
    time.sleep(0.01)

def RIGHT_TURN(deg):
    full_circle = 510.0
    degree = full_circle / 360 * deg
    GPIO_SETUP(0, 0, 0, 0)

    for i in range(int(degree)):
        GPIO_SETUP(1, 0, 0, 0)
        GPIO_SETUP(1, 1, 0, 0)
        GPIO_SETUP(0, 1, 0, 0)
        GPIO_SETUP(0, 1, 1, 0)
        GPIO_SETUP(0, 0, 1, 0)
        GPIO_SETUP(0, 0, 1, 1)
        GPIO_SETUP(0, 0, 0, 1)
        GPIO_SETUP(1, 0, 0, 1)

def LEFT_TURN(deg):
    full_circle = 420.0
    degree = full_circle / 360 * deg
    GPIO_SETUP(0, 0, 0, 0)

    for i in range(int(degree)):
        GPIO_SETUP(1, 0, 0, 1)
        GPIO_SETUP(0, 0, 0, 1)
        GPIO_SETUP(0, 0, 1, 1)
        GPIO_SETUP(0, 0, 1, 0)
        GPIO_SETUP(0, 1, 1, 0)
        GPIO_SETUP(0, 1, 0, 0)
        GPIO_SETUP(1, 1, 0, 0)
        GPIO_SETUP(1, 0, 0, 0)


if __name__ == '__main__':
    RIGHT_TURN(90)
    time.sleep(1)
    LEFT_TURN(90)
    GPIO_SETUP(0, 0, 0, 0)
