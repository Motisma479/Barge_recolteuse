import pifacedigitalio
from sys import stdin
import Time
#libairies

pfd= pifacedigitalio.PiFaceDigital()

in1 = sys.stdin #input depuis nodered

def checkstatus (): #fonction pour regarder l'état des relais
    print ('relay1' + str(pfd.output_pins[0].value))
    print ('relay2' + str(pfd.output_pins[1].value))


while True : #boucle principale
    while line in in1 != 'refreshoff':
        checkstatus()
        Time.sleep(1000) #délais de 1000ms
    while line in in1 != 'refreshon' :
        Time.sleep(1000)
