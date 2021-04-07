import imageio
import numpy
from matplotlib.pyplot import *
from tkinter import*

img = imread("../final/capture.png")
Yi,Xi,Ci = tuple(img.shape)
X1 = 0
Y1 = 0
X2 = 0
Y2 = 0
def pointeur1(event):
    global X1
    global Y1
    chaine.configure(text = "Clic détécté en X1 =" + str(event.x) +\
                     ", Y1 =" + str(event.y))
    X1=int(event.x)
    Y1=int(event.y)
    
def pointeur2(event):
    global X2
    global Y2
    chaine.configure(text = "Clic détécté en X2 =" + str(event.x) +\
                     ", Y2 =" + str(event.y))
    X2=int(event.x)
    Y2=int(event.y)
    
def trace():
    monCanvas.delete("Select")
    monCanvas.create_rectangle(X1, Y1, X2, Y2, width=2, fill="#00FFFF", stipple="gray25", tags="Select" )
    print(X1, Y1, X2 ,Y2)
def save():
    if(Y1<Y2 and X1<X2):
        Xt1=str(X1)
        Xt2=str(X2)
        Yt1=str(Y1)
        Yt2=str(Y2)
    else:
        Xt1=str(X1)
        Xt2=str(X2)
        Yt1=str(Y2)
        Yt2=str(Y1)
    fichier = open("selection.txt", "w")
    fichier.write(Yt1);    fichier.write(" ")
    fichier.write(Yt2);    fichier.write(" ")
    fichier.write(Xt1);    fichier.write(" ")
    fichier.write(Xt2)
    fichier.close()

fen_princ = Tk()
fen_princ.title("Selectionneur de zone")


# Création du cadre-conteneur pour les menus

zoneMenu = Frame(fen_princ, borderwidth=1, bg='#303030')
zoneMenu.pack(fill=X)

# Création du boutton Fermer

menuFermer = Button(zoneMenu, text='Fermer', width='20', borderwidth=2, activebackground='#7FFFFF', command = fen_princ.quit, relief = RAISED)
menuFermer.grid(row=0,column=0)


# Création du boutton Trace

menuTrace = Button(zoneMenu, text='Trace', width='20', borderwidth=2, activebackground='#7FFFFF', command = trace, relief = RAISED)
menuTrace.grid(row=0,column=1)


# Création du boutton Save

menuSave = Button(zoneMenu, text='Save', width='20', borderwidth=2, activebackground='#7FFFFF', command = save, relief = RAISED)
menuSave.grid(row=0,column=2)

monCanvas = Canvas(fen_princ, width=(Xi), height=(Yi),bg='ivory')#.create_image(50, 50, anchor=NE, image=PhotoImage(file = "image.jpg"))
monCanvas.bind("<Button-1>", pointeur1)

monCanvas.bind("<Button-3>", pointeur2)
monCanvas.pack()

photo = PhotoImage(file="capture.png")
monCanvas.create_image(Xi/2,Yi/2, image=photo)
chaine = Label(fen_princ)
chaine.pack()

fen_princ.mainloop()
