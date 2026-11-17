# Hier werden die erforderlichen Software-Module importiert. Dabei sollte nichts verändert werden
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile

def fahren(ev3, sensor_touch, sensor_farbe, motor_links, motor_rechts):
    while (not sensor_touch.pressed()):
        motor_links.run(600)
        motor_rechts.run(600)
        x = sensor_farbe.color()
        if (x != sensor_farbe.color(BLACK)):
            return
        else:
            break
    else:
        motor_links.Stop
        motor_rechts.Stop
        # scan_position
    

#def stop(ev3, sensor_touch, sensor_farbe, motor_links, motor_rechts):
    #if sensor_touch.pressed()
    #or sensor_farbe.color.black: 
   # stop
