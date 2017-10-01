#file for the coffee maker
import socket
HOST =''
PORT = 6000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.bind((HOST,PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

s.listen(2)

while 1:
    conn, addr = s.accept()
    #start coffee
