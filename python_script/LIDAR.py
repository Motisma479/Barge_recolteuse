from sweeppy import Sweep 

def setspeed(speed) :
    with Sweep("/dev/ttyUSB0") as sweep :
        sweep.set_motor_speed(speed)
        
        
def Start_Stop (x):
    if x == 'Start' or 'start':
        with Sweep("/dev/ttyUSB0") as sweep :
            sweep.start_scanning()
    
    elif x == 'Stop' or 'stop' :
        with Sweep("/dev/ttyUSB0") as sweep :
            sweep.stop_scanning()
              
    
def  Scanparser():
    Scans[]
    with Sweep("/dev/ttyUSB0") as sweep :
        Scans = sweep.get_scans()
        
                 
    