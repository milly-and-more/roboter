from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile
import sensor
import motor
from pybricks.tools import wait, StopWatch, DataLog


class Roboter:
    GRUND_GESCHWINDIGKEIT = 600
    KURVEN_ABSTANDS_VERHAELTNIS = 2.0
    MAX_GESCHWINDIGKEIT = 900
    GERADAUS_NACH_DREHUNG_MSEC = 800
    DREH_ZIELWINKEL = 90
    DREH_TOLERANZ = 1
    DREH_MIN_GESCHWINDIGKEIT = 20


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
            wand_abstand = self.ultraschall.distanz_wand_kontrolle()

            if(wand_abstand > self.ultraschall.PERFEKTE_DISTANZ):      #Abzweigung erkannt
                self.motoren.gerade_fahren(self.GRUND_GESCHWINDIGKEIT)
                while not self.touchsensor.pressed():
                    wait(10)
                self.motoren.beide_stop()
                self.drehen()
                continue

            korrektur = 1 + wand_abstand / self.ultraschall.PERFEKTE_DISTANZ
            korrektur = max(0.5, min(1.5, korrektur))

            rechte_geschwindigkeit = int(self.GRUND_GESCHWINDIGKEIT * korrektur)
            self.motoren.korrigierendes_fahren(self.GRUND_GESCHWINDIGKEIT, rechte_geschwindigkeit)
            wait(10)
                
    def drehen(self):
        self.gyroskop.reset_angle()
        angle = self.gyroskop.get_angle()
        zielwinkel = self.DREH_ZIELWINKEL + self.DREH_TOLERANZ
        while abs(angle) < zielwinkel:
            verbleibender_winkel = zielwinkel - abs(angle)
            geschwindigkeit = max(
                self.DREH_MIN_GESCHWINDIGKEIT,
                int(self.GRUND_GESCHWINDIGKEIT * verbleibender_winkel / self.DREH_ZIELWINKEL),
            )
            self.motoren.links_drehen(geschwindigkeit)
            wait(10)
            angle = self.gyroskop.get_angle()
        
        self.motoren.beide_stop()
        self.motoren.gerade_fahren(self.GRUND_GESCHWINDIGKEIT)
        wait(self.GERADAUS_NACH_DREHUNG_MSEC)
        self.motoren.beide_stop()