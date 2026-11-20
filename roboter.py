from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile
import sensor
import motor    

class Roboter:
    GRUND_GESCHWINDIGKEIT = 300
    KURVEN_ABSTANDS_VERHAELTNIS = 2.0
    MAX_GESCHWINDIGKEIT = 900
    GERADAUS_NACH_DREHUNG_MSEC = 800
    DREH_ZIELWINKEL = 90
    DREH_TOLERANZ = 1
    DREH_MIN_GESCHWINDIGKEIT = 20

    ritturns = 0


    def __init__(self):
        self.touchsensor = sensor.Lanzensensor()
        self.farbsensor = sensor.Farbsensor()
        self.gyroskop = sensor.Gyroskop()
        self.ultraschall = sensor.Ultraschall()
        self.motoren = motor.Motoren()
        self.motormarkierung = motor.MotorMarkierung()

    def start(self):
        while not self.touchsensor.pressed():
            wait(1)
        if self.ultraschall.distanz_wand_kontrolle() > 250:
            self.drehen("links")
            print("1. ja")
        else:
            self.drehen("rechts")
            print("2. nein")
        self.bewegen()

        
    
    def bewegen(self):
        while(True):
            #kontrolle ziel
            if self.farbsensor.recognize_fin():
                self.finish()
                return
            wand_abstand = self.ultraschall.distanz_wand_kontrolle()

            if self.touchsensor.pressed():
                self.ritturns += 1
                self.motoren.beide_stop()
                self.motoren.fahren_gerade_degree(300, -40)
                self.drehen("rechts")
                return
            elif wand_abstand > 250:
                self.ritturns = 0
                self.motoren.beide_stop()
                self.motoren.fahren_gerade_degree(self.GRUND_GESCHWINDIGKEIT, 280)
                self.motoren.beide_stop()
                self.drehen()
                return
            self.ritturns = 0
            korrektur = 1 + wand_abstand / self.ultraschall.PERFEKTE_DISTANZ
            korrektur = max(0.6, min(1.4, korrektur))
            print("korrektur:", korrektur)
            rechte_geschwindigkeit = int(self.GRUND_GESCHWINDIGKEIT * korrektur)
            self.motoren.korrigierendes_fahren(self.GRUND_GESCHWINDIGKEIT, rechte_geschwindigkeit)
                
    def drehen(self, richtung = "links"):
        self.gyroskop.reset_angle()
        angle = self.gyroskop.get_angle()
        zielwinkel = self.DREH_ZIELWINKEL + self.DREH_TOLERANZ
        while True:
            #kontrolle ziel
            if self.farbsensor.recognize_fin():
                self.finish()
                return
            
            verbleibender_winkel = zielwinkel - abs(angle)
            if verbleibender_winkel <= self.DREH_TOLERANZ:
                break
            geschwindigkeit = max(
                self.DREH_MIN_GESCHWINDIGKEIT,
                int(self.GRUND_GESCHWINDIGKEIT * verbleibender_winkel / self.DREH_ZIELWINKEL),
            )
            if richtung == "rechts":
                self.motoren.rechts_drehen(50)
            else:
                self.motoren.links_drehen(geschwindigkeit)
            angle = self.gyroskop.get_angle()
        
        self.motoren.beide_stop()
        if self.ritturns == 2:
            self.motormarkierung.abwurf()
        print("Drehung abgeschlossen. Aktueller Winkel:", angle)
        self.motoren.fahren_gerade_degree(self.GRUND_GESCHWINDIGKEIT, 370)
        self.bewegen()

    def finish(self):
        self.motoren.beide_stop()
        self.motoren.fahren_gerade_degree(200,40)