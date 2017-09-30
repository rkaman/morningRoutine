import datetime
now = datetime.datetime.now()
#alarmHour = getAlarmHour()
#alarmMin = getAlarmMin()
showerDelay = 1
coffeeDelay = 5
if now.hour() == alarmHour and now.minute() == alarmMin:
    """while getMSensor() :
            soundAlarm()
            """

if now.hour == alarmHour and now.minute() == alarmMin-showerDelay :
    #startShower()
    print("shower")
if now.hour == alarmHour and now.minute() == alarmMin-coffeeDelay :
    #startCoffee()
    print("coffee")
