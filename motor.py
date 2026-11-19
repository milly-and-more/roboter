from turtle import speed

from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog


class Motoren:
    def __init__(self):
        self.motor_r = Motor(Port.A)
        self.motor_l = Motor(Port.B)

    def gerade_fahren(self, speed):
        self.motor_l.run(speed)
        self.motor_r.run(speed)
        
        # while not sensor_touch.pressed() and sensor_farbe.color() == Color.BLACK:
        #    wait(10)

    def korrigierendes_fahren(self, speed_l, speed_r):
        self.motor_l.run(speed_l)
        self.motor_r.run(speed_r)

    def links_drehen(self, speed):
        self.motor_l.run(-speed)
        self.motor_r.run(speed)

    def rechts_drehen(self, speed):
        self.motor_l.run(speed)
        self.motor_r.run(-speed)

    def beide_stop(self):
        self.motor_l.hold()
        self.motor_r.hold()

    def beide_bremsen(self):
        self.motor_l.brake()
        self.motor_r.brake()

    def fahren_gerade_degree(self, speed, degree):
        self.motor_l.run_angle(speed, degree, then=Stop.HOLD, wait=False)
        self.motor_r.run_angle(speed, degree, then=Stop.HOLD, wait=True)




class MotorMarkierung:
    def __init__(self):
        self.motor = Motor(Port.C)

    def abwurf(self):
        self.motor.run_time(500, 2000)
        self.motor.stop()