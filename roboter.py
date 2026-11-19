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

            if self.touchsensor.pressed():
                self.motoren.beide_stop()
                self.motoren.fahren_gerade_degree(300, -40)
                self.drehen("rechts")
                continue
            elif wand_abstand > 250:
                self.motoren.beide_stop()
                self.motoren.fahren_gerade_degree(self.GRUND_GESCHWINDIGKEIT, 250)
                self.motoren.beide_stop()
                self.drehen()
                return

            korrektur = 1 + wand_abstand / self.ultraschall.PERFEKTE_DISTANZ
            korrektur = max(0.5, min(1.5, korrektur))

            rechte_geschwindigkeit = int(self.GRUND_GESCHWINDIGKEIT * korrektur)
            self.motoren.korrigierendes_fahren(self.GRUND_GESCHWINDIGKEIT, rechte_geschwindigkeit)
            wait(10)
                
    def drehen(self, richtung = "links"):
        self.gyroskop.reset_angle()
        angle = self.gyroskop.get_angle()
        zielwinkel = self.DREH_ZIELWINKEL + self.DREH_TOLERANZ
        while True:
            verbleibender_winkel = zielwinkel - abs(angle)
            if verbleibender_winkel <= self.DREH_TOLERANZ:
                break
            geschwindigkeit = max(
                self.DREH_MIN_GESCHWINDIGKEIT,
                int(self.GRUND_GESCHWINDIGKEIT * verbleibender_winkel / self.DREH_ZIELWINKEL),
            )
            if richtung == "rechts":
                self.motoren.rechts_drehen(geschwindigkeit)
            else:
                self.motoren.links_drehen(geschwindigkeit)
            wait(10)
            angle = self.gyroskop.get_angle()
        
        self.motoren.beide_stop()
        print("Drehung abgeschlossen. Aktueller Winkel:", angle)
        self.motoren.fahren_gerade_degree(self.GRUND_GESCHWINDIGKEIT, 370)
        self.bewegen()