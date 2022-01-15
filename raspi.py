import RPi.GPIO as GPIO
from time import sleep
import os


GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

while True:

 i = GPIO.input(17)

 if i==1:

  print("Motion Detected")
  os.system('python bot.py')
  sleep(2)
