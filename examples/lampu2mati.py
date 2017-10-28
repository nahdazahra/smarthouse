import RPi.GPIO as GPIO
import time
import logging


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(27, GPIO.OUT)
GPIO.output(27, GPIO.LOW)

LOG="/home/pi/python-telegram-bot/examples/lampu2.log"
logging.basicConfig(filename=LOG, filemode="w", level=logging.INFO, format='%(message)s')
logging.info("Lampu rumah mati")
