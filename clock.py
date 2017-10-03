import datetime
import socket
import pygame
pygame.init()
pygame.mixer.music.load("")
now = datetime.datetime.now()
alarmHour = 8  #getAlarmHour()
alarmMin = 30  #getAlarmMin()
showerDelay = 1
coffeeDelay = 5
sHost = '192.168.1.101'
cHost = '192.168.1.100'
sPort = 6001
cPort = 6000

now = datetime.datetime.now()
#1 to shower sensor starts polling its motion sensor and sending data, play sound until we get a motion detected
if now.hour() == alarmHour and now.minute() == alarmMin:
    s0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s0.connect((sHost,sPort))
    s0.sendall("1")
    pygame.mixer.music.play(-1,0)
    data = s0.recv(8)
    """while data == "0":
        if not pygame.mixer.music.get_busy:
            pygame.mixer.music.play()
        data = s0.recv(8)"""
    pygame.mixer.music.stop()
    s0.close()
    
#once shower module sees a zero from here, it starts up the shower
if now.hour == alarmHour and now.minute() == alarmMin-showerDelay :
    #startShower()
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s1.connect((sHost,sPort))
    s1.sendall("0")
    print("shower")
    s1.close()
    #maybe send an end time or something later on
#as soon as coffee establishes the connection it will turn it on
if now.hour == alarmHour and now.minute() == alarmMin-coffeeDelay :
    #startCoffee()
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect((cHost,cPort))
    c.close()
    print("coffee")
