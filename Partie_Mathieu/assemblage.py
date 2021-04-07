#partie analyse
import imageio
import numpy
from matplotlib.pyplot import *
#partie camera
from picamera import PiCamera
from time import sleep
#variables
xt=0
yt=0

camera = PiCamera()
#camera.resolution = (2048,1024)
camera.rotation = 180
camera.start_preview(fullscreen = False, window = (0, 0, 640, 480))
while True :
    sleep(5)
    camera.capture("../final/capture.png")

    img = imread("../final/capture.png")
    img = imageio.core.image_as_uint(img, 8)

    fichier = open("selection.txt", "r")
    c1,c2,c3,c4 =  fichier.read().split(' ')
    c1=int(c1)
    c2=int(c2)
    c3=int(c3)
    c4=int(c4)
    fichier.close()

    rouge = img[:,:,0]
    vert = img[:,:,1]
    bleu = img[:,:,2]

    partie = rouge[c1 : c2 , c3 : c4]
    Y,X = tuple(partie.shape)

    imageio.imwrite("../final/imzone.png",partie)

    tab_img = [[0 for i in range(X)]for i in range(Y)] #list de la taille de l'image

    while (yt<Y):
        while(xt<X):
            tab_img[yt][xt]=rouge[yt][xt]#analyse du rouge
            xt=xt+1
        xt=0
        yt=yt+1
    yt=0
    ttr=np.sum(tab_img,axis=0)
    ttr=np.sum(ttr)
    ttr=ttr/(X*Y)
    ttr=(ttr*100)/255
    print(ttr)
