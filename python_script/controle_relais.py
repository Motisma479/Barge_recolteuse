import pifacedigitalio #lib pour la carte de relais
import sys

pfd= pifacedigitalio.PiFaceDigital()

in1 = sys.stdin

#fonctions de déclanchement des relais
def actmoteurconv (event):
    event.chip.relays[0].toggle()
    if pfd.output_pins[0].value == 1 :
        print('rl1on')
    elif pfd.output_pins[0].value == 0 :
        print('rl1off')



def actmoteurvibr ():
    pfd.relays[1].toggle()
    if pfd.output_pins[1].value == 1 :
        print('rl2on')
    elif pfd.output_pins[1].value == 0:
        print('rl2off')

def checkstatus ():
    print ('relay1' + str(pfd.output_pins[0].value))
    print ('relay2' + str(pfd.output_pins[1].value))

#listener = pifacedigitalio.InputEventListener(chip=pfd) # system interupt

#listener.register(0, pifacedigitalio.IODIR_FALLING_EDGE, rl1toggle)

#listener.activate()


if __name__ == '__main__':
    for line in in1 :
        if 'q' == line.rstrip():
            break
        if 'moteurconv' == line.rstrip():
            actmoteurconv()
        elif 'moteurvibr' == line.rstrip():
            actmoteurvibr()
        if 'refresh' == line.rstrip():
            checkstatus()

#while (1==1):
#
#     if but1check() == 0 :
#         pfd.relays[1].turn_on()
#         print(bool(but1check()))
#     else :
#         pfd.relays[1].turn_off()
#         print(bool(but1check()))
