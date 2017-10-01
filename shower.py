#file for shower module
HOST =''
PORT = 6001

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.bind((HOST,PORT))
except ocket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

s.listen(2)

while 1:
    conn, addr = s.accept()
    data = conn.recv(8)  #receive a 0 if we want to turn on the shower, 1 if alarm is going off and motion sensor needs to be tripped
    data = int(data)
    if data == 0:
        #turn on shower
    else:
        #while motion sensor not tripped:
        #    conn.sendall("0")????
        conn.sendall("1")
