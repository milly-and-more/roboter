import sensor
import motor

class Roboter:
    def __init__(self):
        self.touchsensor = sensor.Lanzensensor()
        self.farbsensor = sensor.Farbsensor()
        self.gyroskop = sensor.Gyroskop()
        self.ultraschall = sensor.Ultraschall()
        self.motoren = motor.Motoren()
        self.motormarkierung = motor.MotorMarkierung()

    def start(self):
        self.motoren.gerade_fahren(600)
        print(self.farbsensor.get_rgb())
        while(True):
            print(self.gyroskop.get_speed())

    
    def stop(self):
        doof = []
