from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color

#hier sit ein code welcher das gyroskop verwendet

class Lanzensensor:
    def __init__(self):
        self.touchsensor = TouchSensor(Port.S1)

class Farbsensor:
    def __init__(self):
        self.farbsensor = ColorSensor(Port.S2)

    def get_rgb(self):
        return self.farbsensor.rgb()

class Gyroskop:
    def __init__(self):
        self.gyroskop = GyroSensor(Port.S3)

    def get_distance(self):
        return self.gyroskop.distance()

class Ultraschall:
    def __init__(self):
        self.ultraschall =  UltrasonicSensor(Port.S4)


