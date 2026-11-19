# In dieser Datei können eigene Funktionen definiert werden. Es können auch weitere Dateien angelegt werden, die dann in main.py importiert werden müssen

# Hier werden die erforderlichen Software-Module importiert. Dabei sollte nichts verändert werden
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile


def fahre_bis_stop(motor_links, motor_rechts, sensor_touch, sensor_farbe):
    motor_links.run(600)
    motor_rechts.run(600)

   # while not sensor_touch.pressed() and sensor_farbe.color() == Color.BLACK:
    #    wait(10)
    
    motor_links.stop()
    motor_rechts.stop()

def start_durch_klappe(sensor_ultraschall, motor_links, motor_rechts, sensor_touch, sensor_farbe):
    startabstand = sensor_ultraschall.distance()

    if abs(sensor_ultraschall.distance() - startabstand) < 20:
        wait(100)
    fahre_bis_stop(motor_links, motor_rechts, sensor_touch, sensor_farbe)    

    def recognize_fin(self):
    rgb_momentan = sensoren.Farbsensor().get_rgb()
    sum_rgb = (rgb_momentan[0]**2 + rgb_momentan[1]**2 + rgb_momentan[2]**2)**0.5
    sum_s = 30
    if  sum_rgb < sum_s:
        return False
    else:
        return True