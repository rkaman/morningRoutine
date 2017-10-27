from gpiozero import LED
from time import sleep

start = LED(4)
#should see LED on the relay turn on for a second and the turn off
start.on()
sleep(1)
start.off()
