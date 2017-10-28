import RPi.GPIO as GPIO
import time
import logging

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(22, GPIO.OUT)
GPIO.output(22, GPIO.LOW)

LOG="/home/pi/python-telegram-bot/examples/lampu3.log"
logging.basicConfig(filename=LOG, filemode="w", level=logging.INFO, format='%(message)s')
logging.info("Lampu depan mati")

