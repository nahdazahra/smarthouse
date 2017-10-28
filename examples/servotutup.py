import RPi.GPIO as GPIO
import time
import logging

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)

p = GPIO.PWM(23,50)

p.start(2.5)
iterasi = 50
waktu = 2
span = 5/float(iterasi)
span = span*0.8
sleep = waktu/float(iterasi)
for i in range(0,iterasi):
   p.ChangeDutyCycle(2.5+span*i)
   time.sleep(sleep)

LOG="/home/pi/python-telegram-bot/examples/garasi.log"
logging.basicConfig(filename=LOG, filemode="w", level=logging.INFO, format='%(message)s')
logging.info("Garasi tutup")

p.stop()

GPIO.cleanup()
