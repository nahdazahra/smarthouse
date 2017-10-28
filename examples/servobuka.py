import RPi.GPIO as GPIO
import time
import logging

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)

p = GPIO.PWM(23,50)
#dc = 7.5
p.start(7.5)
#LOG="/home/pi/python-telegram-bot/examples/status.log"
iterasi = 50
waktu = 2
span = 5/float(iterasi)
span = span * 1.3
sleep = waktu/float(iterasi)
for i in range(0,iterasi):
   p.ChangeDutyCycle(7.5-span*i)
   time.sleep(sleep)

#print '12.5' >> log.txt
LOG="/home/pi/python-telegram-bot/examples/garasi.log"
logging.basicConfig(filename=LOG, filemode="w", level=logging.INFO, format='%(message)s')
logging.info("Garasi buka")

p.stop()

GPIO.cleanup()
