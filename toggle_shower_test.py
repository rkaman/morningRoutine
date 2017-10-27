from gpiozero import LED
from time import sleep

shower = LED(4)

"""attach valve to shower and turn on.  Should wait 10 seconds
turn on the shower for 10 seconds, then turn back off."""
sleep(10)
shower.on()
sleep(10)
shower.off()
