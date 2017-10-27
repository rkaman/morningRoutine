#file for shower module
import socket
from time import sleep
from gpiozero import MotionSensor, LED
HOST = ''
PORT = 6001

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
pir = MotionSensor(17)
shower = LED(4)
try:
    s.bind((HOST,PORT))
    print("socket bound")
except socket.error:
    print("Bind failed")
    sys.exit()

s.listen(2)
def runShower():
    while 1:
        print("waiting for connection")
        conn, addr = s.accept()
        print("connected")
        data = conn.recv(8)  #receive a 0 if we want to turn on the shower, 1 if alarm is going off and motion sensor needs to be tripped
        input = int(data)
        if input == 1:
            #turn on shower
            shower.on()
            print("shower on")
        if input == 0:
            pir.wait_for_motion()
            """while not pir.motion_detected:
                conn.sendall('0')
                sleep(.1)"""
            conn.sendall(b'1')
        if input == 2 :
            shower.off()
            print("shower off")
        sleep(.1)
runShower()
