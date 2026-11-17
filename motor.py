from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color

class Motoren:
    def __init__(self):
        self.motor_r = Motor(Port.A)
        self.motor_l = Motor(Port.B)

    def gerade_fahren(self, speed):
        self.motor_l.run(speed)
        self.motor_r.run(speed)
        
        # while not sensor_touch.pressed() and sensor_farbe.color() == Color.BLACK:
        #    wait(10)

class MotorMarkierung:
    def __init__(self):
        self.motor = Motor(Port.C)