from sweeppy import Sweep 
import sys

in1 = sys.stdin

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
    Scans=[]
    with Sweep("/dev/ttyUSB0") as sweep :
        Scans = sweep.get_scans()
    return Scans
                 

while True : #boucle principale 
        
        line = input()
        if line == 'Start':
            Start_Stop('Start')
        elif line == 'Stop':
            Start_Stop('Stop')
        elif line == ('Scan'):
            print(Scanparser())
        elif line == 'setspeed':
            setspeed(input('Vitesse de 0 a 10'))
        



