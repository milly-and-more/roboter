import sensor
import motor

class Roboter:
    def __init__(self):
        self.touchsensor = sensor.TouchSensor
        self.farbsensor = sensor.Farbsensor
        self.gyroskop = sensor.GyroSensor
        self.ultraschall = sensor.UltrasonicSensor
        self.motoren = motor.Motoren
        self.motormarkierung = motor.MotorMarkierung

    def start(self):
        self.motoren.gerade_fahren(600)
        self.abstand = self.ultraschall.distance()

    
    def stop(self):
        doof = []
