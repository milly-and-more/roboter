from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color

class Lanzensensor:
    def __init__(self):
        self.touchsensor = TouchSensor(Port.S1)

    def pressed(self):
        return self.touchsensor.pressed()

class Farbsensor:
    def __init__(self):
        self.farbsensor = ColorSensor(Port.S2)  

    def get_rgb(self):
        return self.farbsensor.rgb()

    def get_tages_rgb(self):
        global tagesrgb
        tagesrgb = self.farbsensor.rgb()

    def recognize_fin(self):
        rgb_momentan = self.get_rgb()
        sum_rgb = (rgb_momentan[0]**2 + rgb_momentan[1]**2 + rgb_momentan[2]**2)**0.5
        sum_s = 15
        if  sum_rgb > sum_s:
            return False
        else:
            print("finish" + str(sum_rgb))
            return True

    

class Gyroskop:
    def __init__(self):
        self.gyroskop = GyroSensor(Port.S3)

    def get_speed(self):
        return self.gyroskop.speed()
        
    def get_angle(self):
        return self.gyroskop.angle()

    def reset_angle(self, angle=0):
        self.gyroskop.reset_angle(angle)
    

class Ultraschall:
    PERFEKTE_DISTANZ = 75
    def __init__(self):
        self.ultraschall =  UltrasonicSensor(Port.S4)
    
    def get_distance(self):
        return self.ultraschall.distance()

    def distanz_wand_kontrolle(self):
        """Return the distance devition differenz from the target."""
        aktuelle_distanz = self.get_distance()
        return aktuelle_distanz - self.PERFEKTE_DISTANZ
    
        