#file for the coffee maker
import socket
from gpiozero import LED
HOST = socket.gethostbyname('coffee')
PORT = 6000
start = LED(4)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.bind((HOST,PORT))
except socket.error:
    print("Bind failed")
    sys.exit()

s.listen(2)

while 1:
    conn, addr = s.accept()
    #start coffee
    data = conn.recv(8)  #receive a 0 if we want to turn on the shower, 1 if alarm is going off and motion sensor needs to be tripped
    data = int(data)
    if data == 1 :
        #turn on shower
        start.on()
    if data == 2:
        start.off()
