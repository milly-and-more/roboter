#!/usr/bin/env pybricks-micropython


# Hier werden die erforderlichen Software-Module importiert. Dabei sollte nichts verändert werden
from pybricks.hubs import EV3Brick
#from pybricks.hub import robotics
#from pybricks.hub import parameters
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile


# Hier können Dateien mit eigenen Funktionen importiert werden
from funktionen import *
from scan import *
#from fahren import *
import roboter


# Hier wird die angeschlossene Hardware definiert und konfiguriert
ev3 = EV3Brick()
"""sensor_touch = TouchSensor(Port.S1) # Beispiel für Touch-Sensor an Port S3
motor_links = Motor(Port.B)
motor_rechts = Motor(Port.A)
#sensor_gyroskop = GyroSensor(Port.S2)
sensor_farbe = ColorSensor(Port.S2)
sensor_ultraschall = UltrasonicSensor(Port.S4)
#motor_marke = Motor(Port.B)

#Fahren(ev3, sensor_touch)"""

roboter = roboter.Roboter()
roboter.start()
#roboter.drehen("rechts")

# Ab hier beginnt der eigentliche Programmablauf
""" abstand = abstand_cm(sensor_ultraschall)
ev3.screen.print(str(abstand) + "cm")
start(sensor_ultraschall, motor_links, motor_rechts, sensor_touch, sensor_farbe)
fahren(ev3, sensor_touch, sensor_farbe, motor_links, motor_rechts) """