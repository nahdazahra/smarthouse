import RPi.GPIO as GPIO
import time
import logging

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

GPIO.output(22, GPIO.HIGH)
GPIO.output(17, GPIO.HIGH)
GPIO.output(27, GPIO.HIGH)


#LOG1="/home/pi/python-telegram-bot/examples/lampu1.log"
#logging.basicConfig(filename=LOG1, filemode="w", level=logging.INFO)
#logging.info("Lampu 1 nyala")

#LOG2="/home/pi/python-telegram-bot/examples/lampu2.log"
#logging.basicConfig(filename=LOG2, filemode="w", level=logging.INFO)
#logging.info("Lampu 2 nyala")

#LOG3="/home/pi/python-telegram-bot/examples/lampu3.log"
#logging.basicConfig(filename=LOG3, filemode="w", level=logging.INFO)
#logging.info("Lampu 3 nyala")

