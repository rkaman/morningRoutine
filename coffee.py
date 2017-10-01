#file for the coffee maker
import socket
from gpiozero import LED
HOST =''
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
    start.on()
