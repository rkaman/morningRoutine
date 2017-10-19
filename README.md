# morningRoutine
This project uses Raspberry Pis to automate a basic morning routine.
The basic components are an alarm clock, an automatic shower and an automatic coffee maker.
The alarm clock will not go off until a motion sensor detects movement, and the 
other components are turned on relative to the time of the alarm.

There are currently 4 files within this repo:

clock - contains the python code for checking the time and sending out signals to the coffee
and shower modules to start up their tasks.  This also starts the alarm.   

coffee - contains the code running the coffee maker.  it waits for a connection from the clock
module and using gpio pins turns the coffee maker on and off (in the code the gpio is currently
defined as an LED which just turns the pin high and low when on and off are called respectively)

inputPage - this contains html files to get user input to set the times for the alarms and when 
to turn on the coffee and shower in relation to the alarm.  it also contains python code using Flask
to handle the user inputs.

shower - similarly to the coffee module, this module runs the shower by listening for a connection
from the clock.  This module will turn the shower on and off but also takes input from a motion sensor.
Once the alarm goes off, this module waits to for motion to be detected then sends a signal back
to the clock to turn off the clock.  

This project is being coded in python
