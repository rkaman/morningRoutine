#file for shower module
import socket
from time import sleep
from gpiozero import MotionSensor, LED
HOST ='192.168.1.101'
PORT = 6001

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
pir = MotionSensor(4)
shower = LED(17)
try:
    s.bind((HOST,PORT))
except socket.error:
    print("Bind failed")
    sys.exit()

s.listen(2)
def runShower():
    while 1:
        conn, addr = s.accept()
        data = conn.recv(8)  #receive a 0 if we want to turn on the shower, 1 if alarm is going off and motion sensor needs to be tripped
        data = int(data)
        if data == 1:
            #turn on shower
            shower.on()
        if data == 0:
            pir.wait_for_motion()
            """ while not pir.motion_detected:
                conn.sendall("0")
                sleep(.1)"""
            conn.sendall("1")
        if data == 2 :
            shower.off()


runShower()
