# Hier werden die erforderlichen Software-Module importiert. Dabei sollte nichts verändert werden
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile

def abstand_cm(sensor_ultraschall):
    return sensor_ultraschall.distance() / 10

def Farbwert(sensor_farbe,sensor_touch):
    while not sensor_touch.pressed():
        return(sensor_farbe.rgb())
    