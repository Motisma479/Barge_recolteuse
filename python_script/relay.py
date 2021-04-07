import pifacedigitalio
import sys

pfd= pifacedigitalio.PiFaceDigital()

in1 = sys.stdin


def rl1toggle (event):
    event.chip.relays[0].toggle()
    if pfd.output_pins[0].value == 1 :
        print('rl1on')
    elif pfd.output_pins[0].value == 0 :
        print('rl1off')

    
    
def rl2toggle ():
    pfd.relays[1].toggle()
    if pfd.output_pins[1].value == 1 :
        print('rl2on')
    elif pfd.output_pins[1].value == 0:
        print('rl2off')

    
    
listener = pifacedigitalio.InputEventListener(chip=pfd) # system interupt 

listener.register(0, pifacedigitalio.IODIR_FALLING_EDGE, rl1toggle)

def but1check():
    return(pfd.input_pins[1].value)

listener.activate()

for line in in1 :
    if 'q' == line.rstrip():
        break
    if 'test1' == line.rstrip():
        rl2toggle()
    
    
#while (1==1):
#     
#     if but1check() == 0 :
#         pfd.relays[1].turn_on()
#         print(bool(but1check()))
#     else :
#         pfd.relays[1].turn_off()
#         print(bool(but1check()))

    