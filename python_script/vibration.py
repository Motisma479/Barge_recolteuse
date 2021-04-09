import pifacedigitalio #lib pour la carte de relais
import sys
import time


pfd= pifacedigitalio.PiFaceDigital()

in1 = sys.stdin

def motvibron ():
    pfd.relays[1].turn_on()

def motvibroff ():
    pfd.relays[1].turn_off()



while True : #boucle principale
    while True :
        if pfd.output_pins[1].value == 1:
            motvibroff()
            time.sleep(1)
        else :
            time.sleep(1)

        if in1.read() =='Benne_pleine' :
            break

    while True :
        t= time.time()
        if pfd.output_pins[1].value == 0:
            motvibron()
            time.sleep(1)
        else :
            time.sleep(1)
        t2 = time.time()
        if t2 >= t + 30 :
            print('Benne_pleine')

        if in1.read() =='Benne_non_pleine' :
            break
