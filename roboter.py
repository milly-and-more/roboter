import sensor
import motor

class Roboter:
    GRUND_GESCHWINDIGKEIT = 600


    def __init__(self):
        self.touchsensor = sensor.Lanzensensor()
        self.farbsensor = sensor.Farbsensor()
        self.gyroskop = sensor.Gyroskop()
        self.ultraschall = sensor.Ultraschall()
        self.motoren = motor.Motoren()
        self.motormarkierung = motor.MotorMarkierung()

    def start(self):
        self.motoren.gerade_fahren(self.GRUND_GESCHWINDIGKEIT)
        print(self.farbsensor.get_rgb())
        self.bewegen()

    def bewegen(self):
        while(True):
            wand_abstand = self.ultraschall.distanz_wand_kontrolle();
            if(wand_abstand > 2):
                print("Abzweigung erkannt")


            self.motoren.korrigierendes_fahren(self.GRUND_GESCHWINDIGKEIT, self.GRUND_GESCHWINDIGKEIT * wand_abstand)
            wait(10)

    def drehen(self):
        self.gyroskop.reset_angle(0)
        self.motoren.links_drehen(self.GRUND_GESCHWINDIGKEIT / 4)
        angle = self.gyroskop.get_angle()
        while(angle > -90 | angle < 90): #falsches löschen
            print("Winkel Drehung: " + angle)
            #Abchecken welche Werte ausgegeben werden bei counterclockwise drehung
            wait(2)
            angle = self.gyroskop.get_angle()
        self.bewegen()


    def stop(self):
        doof = []