import pifacedigitalio
from sys import stdin
import time
#libairies

pfd= pifacedigitalio.PiFaceDigital()

in1 = sys.stdin #input depuis nodered

def checkstatus (): #fonction pour regarder l'état des relais
    print ('relay1' + str(pfd.output_pins[0].value))
    print ('relay2' + str(pfd.output_pins[1].value))


while True : #boucle principale
    while line in in1 != 'refreshoff':
        checkstatus()
        time.sleep(1) #délais de 1s
    while line in in1 != 'refreshon' :
        time.sleep(1)
