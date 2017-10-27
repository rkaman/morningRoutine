from gpiozero import MotionSensor
from time import sleep

pir = MotionsSensor(17)

#want to give time to have an empty room to make sure the motion sensor is picking up motion properly

sleep(10)
pir.wait_for_motion()
print("motion detected")


