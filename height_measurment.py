import RPi.GPIO as GPIO
import time
import signal
import sys

# use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
pinTrigger = 18
pinEcho = 24
pinBuzz = 19

def close(signal, frame):
	print("\nTurning off ultrasonic distance detection...\n")
	GPIO.cleanup() 
	sys.exit(0)

def get_distance():
    # set Trigger to HIGH
    GPIO.output(pinTrigger, True)
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(pinTrigger, False)

    startTime = time.time()
    stopTime = time.time()

    # save start time
    while 0 == GPIO.input(pinEcho):
        startTime = time.time()

    # save time of arrival
    while 1 == GPIO.input(pinEcho):
        stopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = stopTime - startTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance


def main():

    signal.signal(signal.SIGINT, close)
    # set GPIO input and output channels
    GPIO.setup(pinTrigger, GPIO.OUT)
    GPIO.setup(pinEcho, GPIO.IN)

    print("Hello World!")

    input("Press Enter to continue...")

    initial_distance = get_distance() 
    print(f"Initial distance {initial_distance}")
    
    print("Height will be acquired by subtracting the current measured distance to the initial distance")

    while True:
        input("Press Enter to get height...")
        current_distance = get_distance()
        print(f"Current distance {current_distance}")
        height=initial_distance-current_distance
        print(f"Resultant height = {height} cm")
        
        GPIO.output(pinBuzz, True)
        time.sleep(2)
        GPIO.output(pinBuzz, False)


if __name__ == "__main__":
    main()