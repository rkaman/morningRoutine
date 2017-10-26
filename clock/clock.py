import datetime
import socket
#import pygame
#butthole



class Clock:
        sHost = socket.gethostbyname('shower')
        cHost = socket.gethostbyname('coffee')
        sPort = 6001
        cPort = 6000

        def __init__(self):
                self.alarmHour = 0  #getAlarmHour()
                self.alarmMin = 0 #getAlarmMin()
                self.showerDelay = 0
                self.coffeeDelay = 0
                self.sflag = 0
                self.aflag = 0
                self.cflag = 0
                self.armed = 0
                self.coffeeOn = 0
                self.showerOn = 0
                
        #1 to shower sensor starts polling its motion sensor and sending data, play sound until we get a motion detected
        def checkAlarm(self, now):
                if now.hour() >= alarmHour and now.minute() >= alarmMin and aflag == 1:
                        s0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s0.connect((sHost,sPort))
                        print("connected")
                        s0.sendall(b'0')
                        #pygame.mixer.music.play(-1,0)
                        #data = s0.recv(8)
                        """while data == "0":
                            if not pygame.mixer.music.get_busy:
                                pygame.mixer.music.play()
                            data = s0.recv(8)"""
                        #pygame.mixer.music.stop()
                        s0.close()
                        aflag = 0
                
        #once shower module sees a zero from here, it starts up the shower
        def checkShowerOn(self, now):
                if alarmMin-showerDelay < 0 :
                        carry = 1
                elif alarmMin-showerDelay > 59:
                        carry = -1
                else:
                        carry = 0
                if now.hour >= alarmHour - carry and now.minute() >= alarmMin-showerDelay +60*carry and sflag == 1 :
                        #startShower()
                        s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s1.connect((sHost,sPort))
                        s1.sendall(b'1')
                        print("shower")
                        s1.close()
                        sflag = 0
                        showerOn = 1
            #maybe send an end time or something later on
        #as soon as coffee establishes the connection it will turn it on
        def checkCoffeeOn(self, now):
                if alarmMin-coffeeDelay < 0 :
                        carry = 1
                elif alarmMin-coffeeDelay > 59:
                        carry = -1
                else:
                        carry = 0
                if now.hour >= alarmHour - carry and now.minute() >= alarmMin-coffeeDelay + 60*carry and sflag == 1 :
                        #startCoffee()
                        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        c.connect((cHost,cPort))
                        s1.sendall(b'1')
                        c.close()
                        print("coffee")
                        cflag = 0
                        coffeeOn = 1

        def checkShowerOff(self,now):
                #added this to deal with the case where delay pushed time into a different hour
                if alarmMin-showerDelay < 0 :
                        carry = 1
                elif alarmMin-showerDelay > 59:
                        carry = -1
                else:
                        carry = 0
                if now.hour >= alarmHour-carry and now.minute() >= alarmMin-showerDelay +60*carry and coffeeOn:
                #startShower()
                        s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s1.connect((sHost,sPort))
                        s1.sendall(b'2')
                        print("shower off")
                        s1.close()
                        self.showerOn = 0

        def checkCoffeeOff(self, now):
                if alarmMin-coffeeDelay < 0 :
                        carry = 1
                elif alarmMin-coffeeDelay > 59:
                        carry = -1
                else:
                        carry = 0
                if now.hour >= alarmHour - carry and now.minute() >= alarmMin-coffeeDelay + 60*carry and coffeeOn == 1 :
                        #startCoffee()
                        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        c.connect((cHost,cPort))
                        s1.sendall(b'2')
                        c.close()
                        print("coffee off")
                        self.coffeeOn = 0
                        
        def resetFlags(self):
                if armed:
                        aflag = 1
                        sflag = 1
                        cflag = 1


if __name__ == "__main__":
        
        while True:
                now = datetime.datetime.now()
                #pygame.init()
                #pygame.mixer.music.load("")
                c = Clock()
                c.checkAlarm()
                c.checkShowerOn(now)
                c.checkCoffeeOn(now)
                c.checkShowerOff(now)
                c.checkCoffeeOff(now)
                if now.hour == 0 and now.minute == 0:
                        c.resetFlags()
                sleep(.3)
                
