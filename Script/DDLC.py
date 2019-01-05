#Les Trois Mousquetaires!
from random import *
from tkinter import *
import time
import sys
import os
import ctypes
sys.setrecursionlimit(150000)
#Verification si un joueur est connecté
os.rename('loginin.dll','loginin.txt')
print(os.path.getsize("loginin.txt"))
if os.path.getsize("loginin.txt") == 0:
    print("Veuillez lancer à partir du launcher")
    ctypes.windll.user32.MessageBoxW(0, "Veuillez lancer le jeu à partir du launcher.", "Memories", 0x40 | 0x0)
    os.rename('loginin.txt','loginin.dll')
    sys.exit("Linkstart")
else:
    listelog2 = open("loginin.txt","r")
    contenuelog = listelog2.read()
    listelog2.close()
    os.rename('loginin.txt','loginin.dll')




fenetre = Tk()
fenetre.title("Memories")
fenetre.iconbitmap("img/icon.ico")
fenetre.configure(width=800,height=600)
backg = PhotoImage(file="img/back.gif")
canvas = Canvas(fenetre)
canvas.place(x=-10,y=-10)
canvas.config(width=810,height=610,bg="blue" )
canvas.create_image(410,310,image = backg)
print(contenuelog)

#Recupèr le meilleur score du joueur connecté
os.rename("compte/"+contenuelog+".dll","compte/"+contenuelog+".txt")
getpointmenu = open("compte/"+str(contenuelog)+".txt","r")
meilleurscoredujoueur = getpointmenu.read()
if meilleurscoredujoueur == "":
    meilleurscoredujoueur = "0"
getpointmenu.close()
os.rename("compte/"+contenuelog+".txt","compte/"+contenuelog+".dll")

imageblanc = PhotoImage(file="img/blanc3.gif")
imageblanc2 = PhotoImage(file="img/blancm.gif")


imageblanc = PhotoImage(file="img/blanc3.gif")
un = PhotoImage(file="img/un.gif")
deux = PhotoImage(file="img/deux.gif")
trois = PhotoImage(file="img/trois.gif")
quatre = PhotoImage(file="img/quatre.gif")
cinq = PhotoImage(file="img/cinq.gif")
six = PhotoImage(file="img/six.gif")
sept = PhotoImage(file="img/sept.gif")
huit = PhotoImage(file="img/huit.gif")
neuf = PhotoImage(file="img/neuf.gif")
dix = PhotoImage(file="img/dix.gif")

argentine = PhotoImage(file="img/argentine.gif")
cambodge = PhotoImage(file="img/cambodge.gif")
cameroun = PhotoImage(file="img/cameroun.gif")
cuba = PhotoImage(file="img/cuba.gif")
grece = PhotoImage(file="img/grece.gif")
madagascar = PhotoImage(file="img/madagascar.gif")
serbie = PhotoImage(file="img/serbie.gif")
sicile = PhotoImage(file="img/sicile.gif")
srilanka = PhotoImage(file="img/sri lanka.gif")
suede = PhotoImage(file="img/suede.gif")
tahti = PhotoImage(file="img/taiti.gif")
taiwan = PhotoImage(file="img/taiwan.gif")
surimane = PhotoImage(file="img/surimane.gif")
lesotho = PhotoImage(file="img/lesotho.gif")
oman = PhotoImage(file="img/dOman.gif")
bouthan = PhotoImage(file="img/lebouthan.gif")


antilope = PhotoImage(file="img/antilopegood.gif")
autruche = PhotoImage(file="img/autruche.gif")
chat =     PhotoImage(file="img/chat.gif")
girafe =   PhotoImage(file="img/girafe_400.gif")
koala =    PhotoImage(file="img/koala.gif")
lemurien = PhotoImage(file="img/lemurien.gif")
panda =    PhotoImage(file="img/panda roux.gif")
reptile =  PhotoImage(file="img/reptile.gif")
fourmi = PhotoImage(file="img/fourmi.gif")
chien = PhotoImage(file="img/chien.gif")




titlem = PhotoImage(file="img/title.gif")
playb = PhotoImage(file="img/playb.gif")
playb2 = PhotoImage(file="img/playb2.gif")
playb3 = PhotoImage(file="img/playb3.gif")
menub = PhotoImage(file="img/menub.gif")
valid = PhotoImage(file="img/valider.gif")
j1w = PhotoImage(file="img/j1w.gif")
j2w = PhotoImage(file="img/j2w.gif")
resetb = PhotoImage(file="img/rejouerb.gif")
even = PhotoImage(file="img/even.gif")


carte =[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]
cartetirage =[]
joueur = 1
i=0
tour = 0
memoire = 0
memoireNom = 0
memoireNom2 = 0
memoirex = 0
memoirey = 0
pointj1 = 0
pointj2 = 0
match = 0




def jouer():
    global carte
    global cartetirage
    global joueur
    global meilleurscoredujoueur
    global resetboutton
    tourtext.place(x=285,y=5)
    carte =[un,un,deux,deux,trois,trois,quatre,quatre,cinq,cinq,six,six,sept,sept,huit,huit,neuf,neuf,dix,dix]
    cartetirage =[]
    choix = 0
    for i in range(20):
        choix = choice(carte)
        cartetirage.append(choix)
        carte.remove(choix)
        choix = 0
        print(cartetirage)
    boutonjouer.place_forget()
    boutonjouer2.place_forget()
    boutonjouer3.place_forget()
    canvas.delete(titlemenu)
    image1.place(x=200,y=50)
    image2.place(x=280,y=50)
    image3.place(x=360,y=50)
    image4.place(x=440,y=50)
    image5.place(x=520,y=50)
    image6.place(x=200,y=155)
    image7.place(x=280,y=155)
    image8.place(x=360,y=155)
    image9.place(x=440,y=155)
    image10.place(x=520,y=155)
    image11.place(x=200,y=260)
    image12.place(x=280,y=260)
    image13.place(x=360,y=260)
    image14.place(x=440,y=260)
    image15.place(x=520,y=260)
    image16.place(x=200,y=365)
    image17.place(x=280,y=365)
    image18.place(x=360,y=365)
    image19.place(x=440,y=365)
    image20.place(x=520,y=365)
    boutonMenu.place(x=10,y=480)
    scorej1.place(x=80,y=130)
    scorej2.place(x=675,y=130)
    joueur1t.place(x=40,y=70)
    joueur2t.place(x=605,y=70)
    joueurco.place_forget()
    meilleurscore.place_forget()
    resetboutton.configure(command = reset)


def jouer2():
    global carte
    global cartetirage
    global joueur
    canvas.config(width=1280,height=610,bg="#2f009a" )
    fenetre.configure(width=1270,height=600)
    tourtext.place(x=385,y=5)
    carte =[argentine,argentine,cambodge,cambodge,cameroun,cameroun,cuba,cuba,grece,grece,madagascar,madagascar,serbie,serbie,sicile,sicile,srilanka,srilanka,suede,suede,tahti,tahti,taiwan,taiwan,surimane,surimane,lesotho,lesotho,oman,oman,bouthan,bouthan]
    cartetirage =[]
    choix = 0
    for i in range(32):
        choix = choice(carte)
        cartetirage.append(choix)
        carte.remove(choix)
        choix = 0
        print(cartetirage)
    boutonjouer2.place_forget()
    boutonjouer.place_forget()
    boutonjouer3.place_forget()
    joueurco.place_forget()
    meilleurscore.place_forget()
    canvas.delete(titlemenu)
    image1.place(x=200,y=50)
    image2.place(x=286,y=118)
    image3.place(x=372,y=50)
    image4.place(x=456,y=118)
    image5.place(x=542,y=50)
    image6.place(x=628,y=118)
    image7.place(x=200,y=187)
    image8.place(x=372,y=187)
    image9.place(x=543,y=187)
    image10.place(x=286,y=258)
    image11.place(x=458,y=258)
    image12.place(x=628,y=258)
    image13.place(x=200,y=330)
    image14.place(x=372,y=328)
    image15.place(x=542,y=328)
    image16.place(x=286,y=398)
    image17.place(x=456,y=398)
    image18.place(x=628,y=398)
    image19.place(x=714,y=50)
    image20.place(x=714,y=187)
    image21.place(x=714,y=330)
    image22.place(x=200,y=468)
    image23.place(x=372,y=468)
    image24.place(x=542,y=468)
    image25.place(x=714,y=468)
    image26.place(x=800,y=118)
    image27.place(x=800,y=258)
    image28.place(x=800,y=398)
    image29.place(x=884,y=50)
    image30.place(x=884,y=187)
    image31.place(x=884,y=330)
    image32.place(x=884,y=468)
    image1.configure(image = imageblanc2,command=lambda:pick2(image1))
    image2.configure(image = imageblanc2,command=lambda:pick2(image2))
    image3.configure(image = imageblanc2,command=lambda:pick2(image3))
    image4.configure(image = imageblanc2,command=lambda:pick2(image4))
    image5.configure(image = imageblanc2,command=lambda:pick2(image5))
    image6.configure(image = imageblanc2,command=lambda:pick2(image6))
    image7.configure(image = imageblanc2,command=lambda:pick2(image7))
    image8.configure(image = imageblanc2,command=lambda:pick2(image8))
    image9.configure(image = imageblanc2,command=lambda:pick2(image9))
    image10.configure(image = imageblanc2,command=lambda:pick2(image10))
    image11.configure(image = imageblanc2,command=lambda:pick2(image11))
    image12.configure(image = imageblanc2,command=lambda:pick2(image12))
    image13.configure(image = imageblanc2,command=lambda:pick2(image13))
    image14.configure(image = imageblanc2,command=lambda:pick2(image14))
    image15.configure(image = imageblanc2,command=lambda:pick2(image15))
    image16.configure(image = imageblanc2,command=lambda:pick2(image16))
    image17.configure(image = imageblanc2,command=lambda:pick2(image17))
    image18.configure(image = imageblanc2,command=lambda:pick2(image18))
    image19.configure(image = imageblanc2,command=lambda:pick2(image19))
    image20.configure(image = imageblanc2,command=lambda:pick2(image20))
    image21.configure(image = imageblanc2,command=lambda:pick2(image21))
    image22.configure(image = imageblanc2,command=lambda:pick2(image22))
    image23.configure(image = imageblanc2,command=lambda:pick2(image23))
    image24.configure(image = imageblanc2,command=lambda:pick2(image24))
    image25.configure(image = imageblanc2,command=lambda:pick2(image25))
    image26.configure(image = imageblanc2,command=lambda:pick2(image26))
    image27.configure(image = imageblanc2,command=lambda:pick2(image27))
    image28.configure(image = imageblanc2,command=lambda:pick2(image28))
    image29.configure(image = imageblanc2,command=lambda:pick2(image29))
    image30.configure(image = imageblanc2,command=lambda:pick2(image30))
    image31.configure(image = imageblanc2,command=lambda:pick2(image31))
    image32.configure(image = imageblanc2,command=lambda:pick2(image32))

    boutonMenu.place(x=10,y=480)
    scorej1.place(x=80,y=130)
    scorej2.place(x=1100,y=130)
    joueur1t.place(x=10,y=70)
    joueur2t.place(x=1000,y=70)
    resetboutton.configure(command = reset2)

def jouer3():
    global carte
    global cartetirage
    global joueur
    tourtext.place(x=285,y=5)
    carte =[antilope,antilope,autruche,autruche,chat,chat,girafe,girafe,koala,koala,lemurien,lemurien,panda,panda,reptile,reptile,fourmi,fourmi,chien,chien]
    cartetirage =[]
    choix = 0
    for i in range(20):
        choix = choice(carte)
        cartetirage.append(choix)
        carte.remove(choix)
        choix = 0
        print(cartetirage)
    boutonjouer2.place_forget()
    boutonjouer.place_forget()
    boutonjouer3.place_forget()
    canvas.delete(titlemenu)
    image1.place(x=200,y=50)
    image2.place(x=280,y=50)
    image3.place(x=360,y=50)
    image4.place(x=440,y=50)
    image5.place(x=520,y=50)
    image6.place(x=200,y=155)
    image7.place(x=280,y=155)
    image8.place(x=360,y=155)
    image9.place(x=440,y=155)
    image10.place(x=520,y=155)
    image11.place(x=200,y=260)
    image12.place(x=280,y=260)
    image13.place(x=360,y=260)
    image14.place(x=440,y=260)
    image15.place(x=520,y=260)
    image16.place(x=200,y=365)
    image17.place(x=280,y=365)
    image18.place(x=360,y=365)
    image19.place(x=440,y=365)
    image20.place(x=520,y=365)
    boutonMenu.place(x=10,y=480)
    scorej1.place(x=80,y=130)
    scorej2.place(x=675,y=130)
    joueur1t.place(x=40,y=70)
    joueur2t.place(x=605,y=70)
    joueurco.place_forget()
    meilleurscore.place_forget()
    resetboutton.configure(command = reset3)



def menu():
    global w1
    global w2
    global even1
    global tour
    global memoire
    global memoireNom
    global memoireNom2
    global memoirex
    global memoirey
    global joueur
    global pointj1
    global pointj2
    global match
    global carte
    global cartetirage
    global choix
    global titlemenu
    fenetre.configure(width=800,height=600)
    os.rename("compte/"+contenuelog+".dll","compte/"+contenuelog+".txt")
    getpointmenu = open("compte/"+str(contenuelog)+".txt","r")
    meilleurscoredujoueur = getpointmenu.read()
    if meilleurscoredujoueur == "":
        meilleurscoredujoueur = "0"
    getpointmenu.close()
    os.rename("compte/"+contenuelog+".txt","compte/"+contenuelog+".dll")
    joueurco.place(x=290,y=215)
    meilleurscore.place(x=215,y=250)
    meilleurscore.config(text="Votre meilleur score est "+ meilleurscoredujoueur)
    boutonMenu.place_forget()
    image1.place_forget()
    image2.place_forget()
    image3.place_forget()
    image4.place_forget()
    image5.place_forget()
    image6.place_forget()
    image7.place_forget()
    image8.place_forget()
    image9.place_forget()
    image10.place_forget()
    image11.place_forget()
    image12.place_forget()
    image13.place_forget()
    image14.place_forget()
    image15.place_forget()
    image16.place_forget()
    image17.place_forget()
    image18.place_forget()
    image19.place_forget()
    image20.place_forget()
    image21.place_forget()
    image22.place_forget()
    image23.place_forget()
    image24.place_forget()
    image25.place_forget()
    image26.place_forget()
    image27.place_forget()
    image28.place_forget()
    image29.place_forget()
    image30.place_forget()
    image31.place_forget()
    image32.place_forget()
    boutonjouer.place(x=290,y=300)
    boutonjouer2.place(x=290,y=370)
    boutonjouer3.place(x=290,y=440)
    scorej1.place_forget()
    scorej2.place_forget()
    tourtext.place_forget()
    joueur1t.place_forget()
    joueur2t.place_forget()
    resetboutton.place_forget()
    joueur = 1
    i=0
    tour = 0
    memoire = 0
    memoireNom = 0
    memoireNom2 = 0
    memoirex = 0
    memoirey = 0
    joueur = 1
    pointj2 = 0
    pointj1 = 0
    match = 0
    scorej1.config(text=str(pointj1))
    scorej2.config(text=str(pointj2))
    tourtext.config(text="Tour du joueur "+ contenuelog)
    titlemenu = canvas.create_image(400,150,image = titlem)
    canvas.delete(w1)
    canvas.delete(w2)
    canvas.delete(even1)
    validation.place_forget()
    validation2.place_forget()
    image1.configure(image=imageblanc,command=lambda:pick(image1))
    image2.configure(image=imageblanc,command=lambda:pick(image2))
    image3.configure(image=imageblanc,command=lambda:pick(image3))
    image4.configure(image=imageblanc,command=lambda:pick(image4))
    image5.configure(image=imageblanc,command=lambda:pick(image5))
    image6.configure(image=imageblanc,command=lambda:pick(image6))
    image7.configure(image=imageblanc,command=lambda:pick(image7))
    image8.configure(image=imageblanc,command=lambda:pick(image8))
    image9.configure(image=imageblanc,command=lambda:pick(image9))
    image10.configure(image=imageblanc,command=lambda:pick(image10))
    image11.configure(image=imageblanc,command=lambda:pick(image11))
    image12.configure(image=imageblanc,command=lambda:pick(image12))
    image13.configure(image=imageblanc,command=lambda:pick(image13))
    image14.configure(image=imageblanc,command=lambda:pick(image14))
    image15.configure(image=imageblanc,command=lambda:pick(image15))
    image16.configure(image=imageblanc,command=lambda:pick(image16))
    image17.configure(image=imageblanc,command=lambda:pick(image17))
    image18.configure(image=imageblanc,command=lambda:pick(image18))
    image19.configure(image=imageblanc,command=lambda:pick(image19))
    image20.configure(image=imageblanc,command=lambda:pick(image20))

def ident(cartechoisie):
    if cartechoisie == image1:
        return cartetirage[0]
    if cartechoisie == image2:
        return cartetirage[1]
    if cartechoisie == image3:
        return cartetirage[2]
    if cartechoisie == image4:
        return cartetirage[3]
    if cartechoisie == image5:
        return cartetirage[4]
    if cartechoisie == image6:
        return cartetirage[5]
    if cartechoisie == image7:
        return cartetirage[6]
    if cartechoisie == image8:
        return cartetirage[7]
    if cartechoisie == image9:
        return cartetirage[8]
    if cartechoisie == image10:
        return cartetirage[9]
    if cartechoisie == image11:
        return cartetirage[10]
    if cartechoisie == image12:
        return cartetirage[11]
    if cartechoisie == image13:
        return cartetirage[12]
    if cartechoisie == image14:
        return cartetirage[13]
    if cartechoisie == image15:
        return cartetirage[14]
    if cartechoisie == image16:
        return cartetirage[15]
    if cartechoisie == image17:
        return cartetirage[16]
    if cartechoisie == image18:
        return cartetirage[17]
    if cartechoisie == image19:
        return cartetirage[18]
    if cartechoisie == image20:
        return cartetirage[19]
    if cartechoisie == image21:
        return cartetirage[20]
    if cartechoisie == image22:
        return cartetirage[21]
    if cartechoisie == image23:
        return cartetirage[22]
    if cartechoisie == image24:
        return cartetirage[23]
    if cartechoisie == image25:
        return cartetirage[24]
    if cartechoisie == image26:
        return cartetirage[25]
    if cartechoisie == image27:
        return cartetirage[26]
    if cartechoisie == image28:
        return cartetirage[27]
    if cartechoisie == image29:
        return cartetirage[28]
    if cartechoisie == image30:
        return cartetirage[29]
    if cartechoisie == image31:
        return cartetirage[30]
    if cartechoisie == image32:
        return cartetirage[31]

def coordx(xi):
    if xi == image1 or xi == image6 or xi == image11 or xi == image16 or xi == image23:
        return 200
    if xi == image2 or xi == image7 or xi == image12 or xi == image17:
        return 280
    if xi == image3 or xi == image8 or xi == image13 or xi == image18:
        return 360
    if xi == image23:
        return 372
    if xi == image4 or xi == image9 or xi == image14 or xi == image19:
        return 440
    if xi == image5 or xi == image10 or xi == image15 or xi == image20:
        return 520
    if xi == image24:
        return 542
    if xi == image21 or xi == image25:
        return 714
    if xi == image26 or xi == image27 or xi == image28:
        return 800
    if xi == image29 or xi == image30 or xi == image31 or xi == image32:
        return 884

def coordy(yi):
    if yi == image1 or yi == image2 or yi == image3 or yi == image4 or yi == image5 or yi == image29:
        return 50
    if yi == image6 or yi == image7 or yi == image8 or yi == image9 or yi == image10:
        return 155
    if yi == image26:
    	return 118
    if yi == image30:
    	return 187
    if yi == image11 or yi == image12 or yi == image13 or yi == image14 or yi == image15:
        return 260
    if yi == image16 or yi == image17 or yi == image18 or yi == image19 or yi == image20 or yi == image21 or yi == image3:
        return 330
    if yi == image16 or yi == image17 or yi == image18 or yi == image19 or yi == image20:
        return 365
    if yi == image22 or yi == image23 or yi == image24 or yi == image25 or yi == image32:
        return 468
    





def getname(nom):
    if nom == image1:
        return "image1"
    if nom == image2:
        return "image2"
    if nom == image3:
        return "image3"
    if nom == image4:
        return "image4"
    if nom == image5:
        return "image5"
    if nom == image6:
        return "image6"
    if nom == image7:
        return "image7"
    if nom == image8:
        return "image8"
    if nom == image9:
        return "image9"
    if nom == image10:
        return "image10"
    if nom == image11:
        return "image11"
    if nom == image12:
        return "image12"
    if nom == image13:
        return "image13"
    if nom == image14:
        return "image14"
    if nom == image15:
        return "image15"
    if nom == image16:
        return "image16"
    if nom == image17:
        return "image17"
    if nom == image18:
        return "image18"
    if nom == image19:
        return "image19"
    if nom == image20:
        return "image20"
    if nom == image21:
        return "image21"
    if nom == image22:
        return "image22"
    if nom == image23:
        return "image23"
    if nom == image24:
        return "image24"
    if nom == image25:
        return "image25"
    if nom == image26:
        return "image26"
    if nom == image27:
        return "image27"
    if nom == image28:
        return "image28"
    if nom == image29:
        return "image29"
    if nom == image30:
        return "image30"
    if nom == image31:
        return "image31"
    if nom == image32:
        return "image32"
   



def pick(x):
    global tour
    global memoire
    global memoireNom
    global memoireNom2
    global memoirex
    global memoirey
    global joueur
    global pointj1
    global pointj2
    global match
    global w1
    global w2
    global even1
    print("tour du joueur " + str(joueur))
    print("Le joueur 1 a "+str(pointj1)+" points")
    print("Le joueur 2 a "+str(pointj2)+" points")
    tour = tour + 1
    x.configure(image = ident(x),command = 0)
    print("1")
    if tour == 1:
        memoireNom = getname(x)
        memoire = ident(x)
        memoirex = coordx(x)
        memoirey = coordy(x)
    if tour == 2:
        memoireNom2 = getname(x)
        image1.configure(command=0)
        image2.configure(command=0)
        image3.configure(command=0)
        image4.configure(command=0)
        image5.configure(command=0)
        image6.configure(command=0)
        image7.configure(command=0)
        image8.configure(command=0)
        image9.configure(command=0)
        image10.configure(command=0)
        image11.configure(command=0)
        image12.configure(command=0)
        image13.configure(command=0)
        image14.configure(command=0)
        image15.configure(command=0)
        image16.configure(command=0)
        image17.configure(command=0)
        image18.configure(command=0)
        image19.configure(command=0)
        image20.configure(command=0)





        if ident(x) == memoire:

            print("Match")
            match = match + 1
            eval(str(memoireNom)+".place_forget()")
            eval(str(memoireNom2)+".place_forget()")
            image1.configure(command=lambda:pick(image1))
            image2.configure(command=lambda:pick(image2))
            image3.configure(command=lambda:pick(image3))
            image4.configure(command=lambda:pick(image4))
            image5.configure(command=lambda:pick(image5))
            image6.configure(command=lambda:pick(image6))
            image7.configure(command=lambda:pick(image7))
            image8.configure(command=lambda:pick(image8))
            image9.configure(command=lambda:pick(image9))
            image10.configure(command=lambda:pick(image10))
            image11.configure(command=lambda:pick(image11))
            image12.configure(command=lambda:pick(image12))
            image13.configure(command=lambda:pick(image13))
            image14.configure(command=lambda:pick(image14))
            image15.configure(command=lambda:pick(image15))
            image16.configure(command=lambda:pick(image16))
            image17.configure(command=lambda:pick(image17))
            image18.configure(command=lambda:pick(image18))
            image19.configure(command=lambda:pick(image19))
            image20.configure(command=lambda:pick(image20))


            if joueur == 1:
                pointj1 = pointj1 + 10
                tourtext.config(text="Tour du joueur "+ contenuelog)
            if joueur == 2:
                pointj2 = pointj2 + 10
                tourtext.config(text="Tour du joueur "+ str(joueur))
            scorej1.config(text=str(pointj1))
            scorej2.config(text=str(pointj2))
            if match ==10 :
                print("Fin du jeu")
                resetboutton.place(x=200,y=480)
                if pointj1 > pointj2:
                    w1 = canvas.create_image(100,300,image = j1w)
                if pointj2 > pointj1:
                    w1 = canvas.create_image(700,300,image = j1w)
                if pointj1 == pointj2:
                    even1 = canvas.create_image(600,540,image = even)
                os.rename("compte/"+contenuelog+".dll","compte/"+contenuelog+".txt")
                getpoint = open("compte/"+str(contenuelog)+".txt","r")
                getpoint2 = getpoint.read()
                getpoint.close()
                if getpoint2 == "":
                    ajoutpoint= open("compte/"+str(contenuelog)+".txt","w")
                    ajoutpoint.write(str(pointj1))
                    ajoutpoint.close()
                elif int(pointj1) > int(getpoint2):
                    ajoutpoint= open("compte/"+str(contenuelog)+".txt","w")
                    ajoutpoint.write(str(pointj1))
                    ajoutpoint.close()

                os.rename("compte/"+contenuelog+".txt","compte/"+contenuelog+".dll")


        else:
            print("No match")
            validation.place(x=300,y=480)
            if joueur == 1:
                joueur = 2
            else:
                joueur = 1

        tour = 0



def pick2(x):
    global tour
    global memoire
    global memoireNom
    global memoireNom2
    global memoirex
    global memoirey
    global joueur
    global pointj1
    global pointj2
    global match
    global w1
    global w2
    global even1
    print("tour du joueur " + str(joueur))
    print("Le joueur 1 a "+str(pointj1)+" points")
    print("Le joueur 2 a "+str(pointj2)+" points")
    tour = tour + 1
    x.configure(image = ident(x),command = 0)
    print("1")
    if tour == 1:
        memoireNom = getname(x)
        memoire = ident(x)
        memoirex = coordx(x)
        memoirey = coordy(x)
    if tour == 2:
        memoireNom2 = getname(x)
        image1.configure(command=0)
        image2.configure(command=0)
        image3.configure(command=0)
        image4.configure(command=0)
        image5.configure(command=0)
        image6.configure(command=0)
        image7.configure(command=0)
        image8.configure(command=0)
        image9.configure(command=0)
        image10.configure(command=0)
        image11.configure(command=0)
        image12.configure(command=0)
        image13.configure(command=0)
        image14.configure(command=0)
        image15.configure(command=0)
        image16.configure(command=0)
        image17.configure(command=0)
        image18.configure(command=0)
        image19.configure(command=0)
        image20.configure(command=0)
        image21.configure(command=0)
        image22.configure(command=0)
        image23.configure(command=0)
        image24.configure(command=0)
        image25.configure(command=0)
        image26.configure(command=0)
        image27.configure(command=0)
        image28.configure(command=0)
        image29.configure(command=0)
        image30.configure(command=0)
        image31.configure(command=0)
        image32.configure(command=0)




        if ident(x) == memoire:
            print("Match")
            match = match + 1
            eval(str(memoireNom)+".place_forget()")
            eval(str(memoireNom2)+".place_forget()")
            image1.configure(command=lambda:pick2(image1))
            image2.configure(command=lambda:pick2(image2))
            image3.configure(command=lambda:pick2(image3))
            image4.configure(command=lambda:pick2(image4))
            image5.configure(command=lambda:pick2(image5))
            image6.configure(command=lambda:pick2(image6))
            image7.configure(command=lambda:pick2(image7))
            image8.configure(command=lambda:pick2(image8))
            image9.configure(command=lambda:pick2(image9))
            image10.configure(command=lambda:pick2(image10))
            image11.configure(command=lambda:pick2(image11))
            image12.configure(command=lambda:pick2(image12))
            image13.configure(command=lambda:pick2(image13))
            image14.configure(command=lambda:pick2(image14))
            image15.configure(command=lambda:pick2(image15))
            image16.configure(command=lambda:pick2(image16))
            image17.configure(command=lambda:pick2(image17))
            image18.configure(command=lambda:pick2(image18))
            image19.configure(command=lambda:pick2(image19))
            image20.configure(command=lambda:pick2(image20))
            image20.configure(command=lambda:pick2(image20))
            image21.configure(command=lambda:pick2(image21))
            image22.configure(command=lambda:pick2(image22))
            image23.configure(command=lambda:pick2(image23))
            image24.configure(command=lambda:pick2(image24))
            image25.configure(command=lambda:pick2(image25))
            image26.configure(command=lambda:pick2(image26))
            image27.configure(command=lambda:pick2(image27))
            image28.configure(command=lambda:pick2(image28))
            image29.configure(command=lambda:pick2(image29))
            image30.configure(command=lambda:pick2(image30))
            image31.configure(command=lambda:pick2(image31))
            image32.configure(command=lambda:pick2(image32))
            if joueur == 1:
            	tourtext.config(text="Tour du joueur "+ contenuelog)
            	pointj1 = pointj1 + 10
            if joueur == 2:
                pointj2 = pointj2 + 10
                tourtext.config(text="Tour du joueur "+ str(joueur))
            scorej1.config(text=str(pointj1))
            scorej2.config(text=str(pointj2))
            
            if match == 16 :
                print("Fin du jeu")
                validation2.place_forget()
                resetboutton.place(x=200,y=480)
                if pointj1 > pointj2:
                    w1 = canvas.create_image(700,300,image = j1w)
                if pointj2 > pointj1:
                    w1 = canvas.create_image(1125,300,image = j1w)
                if pointj1 == pointj2:
                    even1 = canvas.create_image(600,540,image = even)
                os.rename("compte/"+contenuelog+".dll","compte/"+contenuelog+".txt")
                getpoint = open("compte/"+str(contenuelog)+".txt","r")
                getpoint2 = getpoint.read()
                getpoint.close()
                if getpoint2 == "":
                    ajoutpoint= open("compte/"+str(contenuelog)+".txt","w")
                    ajoutpoint.write(str(pointj1))
                    ajoutpoint.close()
                elif int(pointj1) > int(getpoint2):
                    ajoutpoint= open("compte/"+str(contenuelog)+".txt","w")
                    ajoutpoint.write(str(pointj1))
                    ajoutpoint.close()

                os.rename("compte/"+contenuelog+".txt","compte/"+contenuelog+".dll")


        else:
            print("No match")
            validation2.place(x=1000,y=480)
            if joueur == 1:
                joueur = 2
            else:
                joueur = 1

        tour = 0


def valider():
    eval(str(memoireNom)+".configure(image =imageblanc,command=lambda:pick("+str(memoireNom)+"))")
    eval(str(memoireNom2)+".configure(image =imageblanc,command=lambda:pick("+str(memoireNom2)+"))")
    validation.place_forget()
    image1.configure(command=lambda:pick(image1))
    image2.configure(command=lambda:pick(image2))
    image3.configure(command=lambda:pick(image3))
    image4.configure(command=lambda:pick(image4))
    image5.configure(command=lambda:pick(image5))
    image6.configure(command=lambda:pick(image6))
    image7.configure(command=lambda:pick(image7))
    image8.configure(command=lambda:pick(image8))
    image9.configure(command=lambda:pick(image9))
    image10.configure(command=lambda:pick(image10))
    image11.configure(command=lambda:pick(image11))
    image12.configure(command=lambda:pick(image12))
    image13.configure(command=lambda:pick(image13))
    image14.configure(command=lambda:pick(image14))
    image15.configure(command=lambda:pick(image15))
    image16.configure(command=lambda:pick(image16))
    image17.configure(command=lambda:pick(image17))
    image18.configure(command=lambda:pick(image18))
    image19.configure(command=lambda:pick(image19))
    image20.configure(command=lambda:pick(image20))
    if joueur == 1:
        tourtext.config(text="Tour du joueur "+ contenuelog)
    else:
        tourtext.config(text="Tour du joueur "+ str(joueur))

def valider2():
    eval(str(memoireNom)+".configure(image =imageblanc2,command=lambda:pick("+str(memoireNom)+"))")
    eval(str(memoireNom2)+".configure(image =imageblanc2,command=lambda:pick("+str(memoireNom2)+"))")
    validation2.place_forget()
    image1.configure(command=lambda:pick2(image1))
    image2.configure(command=lambda:pick2(image2))
    image3.configure(command=lambda:pick2(image3))
    image4.configure(command=lambda:pick2(image4))
    image5.configure(command=lambda:pick2(image5))
    image6.configure(command=lambda:pick2(image6))
    image7.configure(command=lambda:pick2(image7))
    image8.configure(command=lambda:pick2(image8))
    image9.configure(command=lambda:pick2(image9))
    image10.configure(command=lambda:pick2(image10))
    image11.configure(command=lambda:pick2(image11))
    image12.configure(command=lambda:pick2(image12))
    image13.configure(command=lambda:pick2(image13))
    image14.configure(command=lambda:pick2(image14))
    image15.configure(command=lambda:pick2(image15))
    image16.configure(command=lambda:pick2(image16))
    image17.configure(command=lambda:pick2(image17))
    image18.configure(command=lambda:pick2(image18))
    image19.configure(command=lambda:pick2(image19))
    image20.configure(command=lambda:pick2(image20))
    image20.configure(command=lambda:pick2(image20))
    image21.configure(command=lambda:pick2(image21))
    image22.configure(command=lambda:pick2(image22))
    image23.configure(command=lambda:pick2(image23))
    image24.configure(command=lambda:pick2(image24))
    image25.configure(command=lambda:pick2(image25))
    image26.configure(command=lambda:pick2(image26))
    image27.configure(command=lambda:pick2(image27))
    image28.configure(command=lambda:pick2(image28))
    image29.configure(command=lambda:pick2(image29))
    image30.configure(command=lambda:pick2(image30))
    image31.configure(command=lambda:pick2(image31))
    image32.configure(command=lambda:pick2(image32))
    if joueur == 1:
        tourtext.config(text="Tour du joueur "+ contenuelog)
    else:
        tourtext.config(text="Tour du joueur "+ str(joueur))

def reset():
    global tour
    global memoire
    global memoireNom
    global memoireNom2
    global memoirex
    global memoirey
    global joueur
    global pointj1
    global pointj2
    global match
    global carte
    global cartetirage
    global choix
    global w1
    global w2
    global even1
    resetboutton.place_forget()
    carte =[un,un,deux,deux,trois,trois,quatre,quatre,cinq,cinq,six,six,sept,sept,huit,huit,neuf,neuf,dix,dix]
    cartetirage =[]
    choix = 0
    for i in range(20):
        choix = choice(carte)
        cartetirage.append(choix)
        carte.remove(choix)
        choix = 0
        print(cartetirage)
    image1.place(x=200,y=50)
    image2.place(x=280,y=50)
    image3.place(x=360,y=50)
    image4.place(x=440,y=50)
    image5.place(x=520,y=50)
    image6.place(x=200,y=155)
    image7.place(x=280,y=155)
    image8.place(x=360,y=155)
    image9.place(x=440,y=155)
    image10.place(x=520,y=155)
    image11.place(x=200,y=260)
    image12.place(x=280,y=260)
    image13.place(x=360,y=260)
    image14.place(x=440,y=260)
    image15.place(x=520,y=260)
    image16.place(x=200,y=365)
    image17.place(x=280,y=365)
    image18.place(x=360,y=365)
    image19.place(x=440,y=365)
    image20.place(x=520,y=365)
    image1.configure(image=imageblanc,command=lambda:pick(image1))
    image2.configure(image=imageblanc,command=lambda:pick(image2))
    image3.configure(image=imageblanc,command=lambda:pick(image3))
    image4.configure(image=imageblanc,command=lambda:pick(image4))
    image5.configure(image=imageblanc,command=lambda:pick(image5))
    image6.configure(image=imageblanc,command=lambda:pick(image6))
    image7.configure(image=imageblanc,command=lambda:pick(image7))
    image8.configure(image=imageblanc,command=lambda:pick(image8))
    image9.configure(image=imageblanc,command=lambda:pick(image9))
    image10.configure(image=imageblanc,command=lambda:pick(image10))
    image11.configure(image=imageblanc,command=lambda:pick(image11))
    image12.configure(image=imageblanc,command=lambda:pick(image12))
    image13.configure(image=imageblanc,command=lambda:pick(image13))
    image14.configure(image=imageblanc,command=lambda:pick(image14))
    image15.configure(image=imageblanc,command=lambda:pick(image15))
    image16.configure(image=imageblanc,command=lambda:pick(image16))
    image17.configure(image=imageblanc,command=lambda:pick(image17))
    image18.configure(image=imageblanc,command=lambda:pick(image18))
    image19.configure(image=imageblanc,command=lambda:pick(image19))
    image20.configure(image=imageblanc,command=lambda:pick(image20))
    joueur = 1
    i=0
    tour = 0
    memoire = 0
    memoireNom = 0
    memoireNom2 = 0
    memoirex = 0
    memoirey = 0
    joueur = 1
    pointj1 = 0
    pointj2 = 0
    match = 0
    scorej1.config(text=str(pointj1))
    scorej2.config(text=str(pointj2))
    canvas.delete(w1)
    canvas.delete(w2)
    canvas.delete(even1)

def reset3():
    global tour
    global memoire
    global memoireNom
    global memoireNom2
    global memoirex
    global memoirey
    global joueur
    global pointj1
    global pointj2
    global match
    global carte
    global cartetirage
    global choix
    global w1
    global w2
    global even1
    resetboutton.place_forget()
    carte =[antilope,antilope,autruche,autruche,chat,chat,girafe,girafe,koala,koala,lemurien,lemurien,panda,panda,reptile,reptile,fourmi,fourmi,chien,chien]
    cartetirage =[]
    choix = 0
    for i in range(20):
        choix = choice(carte)
        cartetirage.append(choix)
        carte.remove(choix)
        choix = 0
        print(cartetirage)
    image1.place(x=200,y=50)
    image2.place(x=280,y=50)
    image3.place(x=360,y=50)
    image4.place(x=440,y=50)
    image5.place(x=520,y=50)
    image6.place(x=200,y=155)
    image7.place(x=280,y=155)
    image8.place(x=360,y=155)
    image9.place(x=440,y=155)
    image10.place(x=520,y=155)
    image11.place(x=200,y=260)
    image12.place(x=280,y=260)
    image13.place(x=360,y=260)
    image14.place(x=440,y=260)
    image15.place(x=520,y=260)
    image16.place(x=200,y=365)
    image17.place(x=280,y=365)
    image18.place(x=360,y=365)
    image19.place(x=440,y=365)
    image20.place(x=520,y=365)
    image1.configure(image=imageblanc,command=lambda:pick(image1))
    image2.configure(image=imageblanc,command=lambda:pick(image2))
    image3.configure(image=imageblanc,command=lambda:pick(image3))
    image4.configure(image=imageblanc,command=lambda:pick(image4))
    image5.configure(image=imageblanc,command=lambda:pick(image5))
    image6.configure(image=imageblanc,command=lambda:pick(image6))
    image7.configure(image=imageblanc,command=lambda:pick(image7))
    image8.configure(image=imageblanc,command=lambda:pick(image8))
    image9.configure(image=imageblanc,command=lambda:pick(image9))
    image10.configure(image=imageblanc,command=lambda:pick(image10))
    image11.configure(image=imageblanc,command=lambda:pick(image11))
    image12.configure(image=imageblanc,command=lambda:pick(image12))
    image13.configure(image=imageblanc,command=lambda:pick(image13))
    image14.configure(image=imageblanc,command=lambda:pick(image14))
    image15.configure(image=imageblanc,command=lambda:pick(image15))
    image16.configure(image=imageblanc,command=lambda:pick(image16))
    image17.configure(image=imageblanc,command=lambda:pick(image17))
    image18.configure(image=imageblanc,command=lambda:pick(image18))
    image19.configure(image=imageblanc,command=lambda:pick(image19))
    image20.configure(image=imageblanc,command=lambda:pick(image20))
    joueur = 1
    i=0
    tour = 0
    memoire = 0
    memoireNom = 0
    memoireNom2 = 0
    memoirex = 0
    memoirey = 0
    joueur = 1
    pointj1 = 0
    pointj2 = 0
    match = 0
    scorej1.config(text=str(pointj1))
    scorej2.config(text=str(pointj2))
    canvas.delete(w1)
    canvas.delete(w2)
    canvas.delete(even1)    

def reset2():
    global tour
    global memoire
    global memoireNom
    global memoireNom2
    global memoirex
    global memoirey
    global joueur
    global pointj1
    global pointj2
    global match
    global carte
    global cartetirage
    global choix
    global w1
    global w2
    global even1
    resetboutton.place_forget()
  	

    carte =[argentine,argentine,cambodge,cambodge,cameroun,cameroun,cuba,cuba,grece,grece,madagascar,madagascar,serbie,serbie,sicile,sicile,srilanka,srilanka,suede,suede,tahti,tahti,taiwan,taiwan,surimane,surimane,lesotho,lesotho,oman,oman,bouthan,bouthan]
    
    cartetirage =[]
    choix = 0
    for i in range(32):
        choix = choice(carte)
        cartetirage.append(choix)
        carte.remove(choix)
        choix = 0
        print(cartetirage)
    boutonjouer2.place_forget()
    boutonjouer.place_forget()
    boutonjouer3.place_forget()
    joueurco.place_forget()
    meilleurscore.place_forget()
    canvas.delete(titlemenu)
    image1.place(x=200,y=50)
    image2.place(x=286,y=118)
    image3.place(x=372,y=50)
    image4.place(x=456,y=118)
    image5.place(x=542,y=50)
    image6.place(x=628,y=118)
    image7.place(x=200,y=187)
    image8.place(x=372,y=187)
    image9.place(x=543,y=187)
    image10.place(x=286,y=258)
    image11.place(x=458,y=258)
    image12.place(x=628,y=258)
    image13.place(x=200,y=330)
    image14.place(x=372,y=328)
    image15.place(x=542,y=328)
    image16.place(x=286,y=398)
    image17.place(x=456,y=398)
    image18.place(x=628,y=398)
    image19.place(x=714,y=50)
    image20.place(x=714,y=187)
    image21.place(x=714,y=330)
    image22.place(x=200,y=468)
    image23.place(x=372,y=468)
    image24.place(x=542,y=468)
    image25.place(x=714,y=468)
    image26.place(x=800,y=118)
    image27.place(x=800,y=258)
    image28.place(x=800,y=398)
    image29.place(x=884,y=50)
    image30.place(x=884,y=187)
    image31.place(x=884,y=330)
    image32.place(x=884,y=468)
    image1.configure(image = imageblanc2,command=lambda:pick2(image1))
    image2.configure(image = imageblanc2,command=lambda:pick2(image2))
    image3.configure(image = imageblanc2,command=lambda:pick2(image3))
    image4.configure(image = imageblanc2,command=lambda:pick2(image4))
    image5.configure(image = imageblanc2,command=lambda:pick2(image5))
    image6.configure(image = imageblanc2,command=lambda:pick2(image6))
    image7.configure(image = imageblanc2,command=lambda:pick2(image7))
    image8.configure(image = imageblanc2,command=lambda:pick2(image8))
    image9.configure(image = imageblanc2,command=lambda:pick2(image9))
    image10.configure(image = imageblanc2,command=lambda:pick2(image10))
    image11.configure(image = imageblanc2,command=lambda:pick2(image11))
    image12.configure(image = imageblanc2,command=lambda:pick2(image12))
    image13.configure(image = imageblanc2,command=lambda:pick2(image13))
    image14.configure(image = imageblanc2,command=lambda:pick2(image14))
    image15.configure(image = imageblanc2,command=lambda:pick2(image15))
    image16.configure(image = imageblanc2,command=lambda:pick2(image16))
    image17.configure(image = imageblanc2,command=lambda:pick2(image17))
    image18.configure(image = imageblanc2,command=lambda:pick2(image18))
    image19.configure(image = imageblanc2,command=lambda:pick2(image19))
    image20.configure(image = imageblanc2,command=lambda:pick2(image20))
    image21.configure(image = imageblanc2,command=lambda:pick2(image21))
    image22.configure(image = imageblanc2,command=lambda:pick2(image22))
    image23.configure(image = imageblanc2,command=lambda:pick2(image23))
    image24.configure(image = imageblanc2,command=lambda:pick2(image24))
    image25.configure(image = imageblanc2,command=lambda:pick2(image25))
    image26.configure(image = imageblanc2,command=lambda:pick2(image26))
    image27.configure(image = imageblanc2,command=lambda:pick2(image27))
    image28.configure(image = imageblanc2,command=lambda:pick2(image28))
    image29.configure(image = imageblanc2,command=lambda:pick2(image29))
    image30.configure(image = imageblanc2,command=lambda:pick2(image30))
    image31.configure(image = imageblanc2,command=lambda:pick2(image31))
    image32.configure(image = imageblanc2,command=lambda:pick2(image32))
    joueur = 1
    i=0
    tour = 0
    memoire = 0
    memoireNom = 0
    memoireNom2 = 0
    memoirex = 0
    memoirey = 0
    joueur = 1
    pointj1 = 0
    pointj2 = 0
    match = 0
    scorej1.config(text=str(pointj1))
    scorej2.config(text=str(pointj2))
    canvas.delete(w1)
    canvas.delete(w2)
    canvas.delete(even1)



titlemenu = canvas.create_image(400,150,image = titlem)

boutonjouer = Button(fenetre, text="Jouer",image =playb,command=jouer,relief="flat",borderwidth=-5,background='#2f009a',activebackground='#2f009a',highlightcolor='#2f009a',highlightthickness=-1)
boutonjouer.place(x=290,y=300)
boutonjouer2 = Button(fenetre, text="Jouer",image =playb2,command=jouer2,relief="flat",borderwidth=-5,background='#2f009a',activebackground='#2f009a',highlightcolor='#2f009a',highlightthickness=-1)
boutonjouer2.place(x=290,y=370)
boutonjouer3 = Button(fenetre, text="Jouer",image =playb3,command=jouer3,relief="flat",borderwidth=-5,background='#2f009a',activebackground='#2f009a',highlightcolor='#2f009a',highlightthickness=-1)
boutonjouer3.place(x=290,y=440)
boutonMenu = Button(fenetre, text="Menu",image = menub ,command=menu,borderwidth=-5,background='#2f009a',relief="flat",activebackground='#2f009a')




joueurco = Label(fenetre, text="Bonjour "+ contenuelog,font=("Verdana", 20),bg="#2f009a")
meilleurscore = Label(fenetre, text="Votre meilleur score est "+ meilleurscoredujoueur ,font=("Verdana", 20),bg="#2f009a")
joueurco.place(x=290,y=215)
meilleurscore.place(x=215,y=250)


tourtext = Label(fenetre, text="Tour du joueur "+ contenuelog,font=("Verdana", 20),bg="#2f009a")
joueur1t = Label(fenetre, text="Score de \n"+contenuelog,font=("Verdana", 17),bg="#2f009a")
joueur2t = Label(fenetre, text="Score Joueur 2",font=("Verdana", 17),bg="#2f009a")
resetboutton = Button(fenetre, image=resetb,command=reset,background='#2f009a',relief="flat",activebackground='#2f009a',borderwidth=-5)
w1 = 0
w2 = 0
even1 = 0

validation = Button(fenetre, image = valid,command=valider,borderwidth=-5,background='#2f009a',relief="flat",activebackground='#2f009a')
validation2 = Button(fenetre, image = valid,command=valider2,borderwidth=-5,background='#2f009a',relief="flat",activebackground='#2f009a')
scorej1 = Label(fenetre,text=str(pointj1),font=("Verdana", 44),bg="#2f009a")
scorej2 = Label(fenetre ,text=str(pointj2),font=("Verdana", 44),bg="#2f009a")
image1 = Button(fenetre, image=imageblanc,command=lambda:pick(image1))
image2 = Button(fenetre, image=imageblanc,command=lambda:pick(image2))
image3 = Button(fenetre, image=imageblanc,command=lambda:pick(image3))
image4 = Button(fenetre, image=imageblanc,command=lambda:pick(image4))
image5 = Button(fenetre, image=imageblanc,command=lambda:pick(image5))
image6 = Button(fenetre, image=imageblanc,command=lambda:pick(image6))
image7 = Button(fenetre, image=imageblanc,command=lambda:pick(image7))
image8 = Button(fenetre, image=imageblanc,command=lambda:pick(image8))
image9 = Button(fenetre, image=imageblanc,command=lambda:pick(image9))
image10= Button(fenetre, image=imageblanc,command=lambda:pick(image10))
image11= Button(fenetre, image=imageblanc,command=lambda:pick(image11))
image12= Button(fenetre, image=imageblanc,command=lambda:pick(image12))
image13= Button(fenetre, image=imageblanc,command=lambda:pick(image13))
image14= Button(fenetre, image=imageblanc,command=lambda:pick(image14))
image15= Button(fenetre, image=imageblanc,command=lambda:pick(image15))
image16= Button(fenetre, image=imageblanc,command=lambda:pick(image16))
image17= Button(fenetre, image=imageblanc,command=lambda:pick(image17))
image18= Button(fenetre, image=imageblanc,command=lambda:pick(image18))
image19= Button(fenetre, image=imageblanc,command=lambda:pick(image19))
image20= Button(fenetre, image=imageblanc,command=lambda:pick(image20))
image21= Button(fenetre, image=imageblanc,command=lambda:pick2(image21))
image22= Button(fenetre, image=imageblanc,command=lambda:pick2(image22))
image23= Button(fenetre, image=imageblanc,command=lambda:pick2(image23))
image24= Button(fenetre, image=imageblanc,command=lambda:pick2(image24))
image25= Button(fenetre, image=imageblanc,command=lambda:pick2(image25))
image26= Button(fenetre, image=imageblanc,command=lambda:pick2(image26))
image27= Button(fenetre, image=imageblanc,command=lambda:pick2(image27))
image28= Button(fenetre, image=imageblanc,command=lambda:pick2(image28))
image29= Button(fenetre, image=imageblanc,command=lambda:pick2(image29))
image30= Button(fenetre, image=imageblanc,command=lambda:pick2(image30))
image31= Button(fenetre, image=imageblanc,command=lambda:pick2(image31))
image32= Button(fenetre, image=imageblanc,command=lambda:pick2(image32))









fenetre.mainloop()