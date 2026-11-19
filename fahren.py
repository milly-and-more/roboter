# Hier werden die erforderlichen Software-Module importiert. Dabei sollte nichts verändert werden
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile

def fahren(ev3, sensor_touch, sensor_farbe, motor_links, motor_rechts):
U = sensor.farbe.rgb()
x = bool(True)
    while (not sensor_touch.pressed() and x):
        motor_links.run(600)           #Fahrtkorrektur ergänzen
        motor_rechts.run(600)
        F = sensor_farbe.rgb()
        rs = 1                          #Werte für schwarz ergänzen
        gs = 4
        bs = 1
        while ([F0]>rs or [F1]>gs or [F2]>bs ):
            pass
        else:
            x = bool(False)
            break
    else:
        motor_links.Stop
        motor_rechts.Stop
        # scan_position
    

#def stop(ev3, sensor_touch, sensor_farbe, motor_links, motor_rechts):
    #if sensor_touch.pressed()
    #or sensor_farbe.color.black: 
   # stop
