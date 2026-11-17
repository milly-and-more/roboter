from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color

class Touchsensor:
    def __init__(self):
        self.touchsensor = TouchSensor(Port.S1)

class Farbsensor:
    def __init__(self):
        self.farbsensor = ColorSensor(Port.S2)

class Gyroskop:
    def __init__(self):
        self.gyroskop = GyroSensor(Port.S3)

class Ultraschall:
    def __init__(self):
        self.ultraschall =  UltrasonicSensor(Port.S4)
