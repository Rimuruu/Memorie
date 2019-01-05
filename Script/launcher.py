# Créé par arenciot, le 27/03/2018 en Python 3.2

import random
from tkinter import *

import sys
import os
import ctypes
sys.setrecursionlimit(150000)

root = Tk()
root.title("Memories")
root.iconbitmap("img/icon.ico")
root.configure(width=800,height=600)
backg = PhotoImage(file="img/back.gif")
canvas = Canvas(root)
canvas.place(x=-10,y=-10)
canvas.config(width=810,height=610,bg="blue" )
canvas.create_image(410,310,image = backg)

loginframe = Canvas(root)
loginframe.place(x=200,y=200)
loginframe.config(width=400,height=200,bg="white" )


NomDeCompte = Entry(root, width = 15,bg = "#BDBDBD",insertofftime=400, relief="flat",font=("verdana",17),)
NomDeCompte.place(x=285,y=250)

MotDePasse = Entry(root, width = 15,bg = "#BDBDBD",insertofftime=400, relief="flat",font=("verdana",17),show = "*")
MotDePasse.place(x=285,y=320)
MotDePassever = Entry(root, width = 15,bg = "#BDBDBD",insertofftime=400, relief="flat",font=("verdana",17))

def create():
    os.rename("Dare.dll","Dare.txt") #Change le dossier Dare.dll en Dare.txt
    listelog2 = open("Dare"+".txt","r") #Lit le dossier Dare.txt
    contenuelog = listelog2.read() #Prend le contenue du dossier
    listelog2.close() #referme le dossier
    nom = NomDeCompte.get() # Récupere le nom de compte de l'utilisateur
    mdp = MotDePasse.get() #récupere le mot de passe
    mdpv = MotDePassever.get() # recup confirmation mot de passe
    #Vérification du contenue et demande de remplir le formulaire
    if str(nom) == "" or str(mdp) == "" or str(mdpv) == "":
    	ctypes.windll.user32.MessageBoxW(None, "Veuillez remplir le formulaire.", "Memories",0x40 | 0x0)
        # il faut que le nom du compte soit de moin de 10 caracteres
    elif len(str(nom)) >= 10:
        ctypes.windll.user32.MessageBoxW(None, "Le nom de compte ne doit pas dépasser les 10 caractères", "Memories",0x40 | 0x0)
#verif  exsistence compt
    elif str(nom) +" "+ str(mdp) in open('Dare.txt').read():
        print("Ce compte existe déjà")
        ctypes.windll.user32.MessageBoxW(None, "Ce compte existe déjà.", "Memories",0x40 | 0x0)
# verif si le nom n'est pas deja utiliser
    elif str(nom) in open("Dare"+".txt").read():
        print("Nom de compte déjà utilisé")
        ctypes.windll.user32.MessageBoxW(None, "Ce nom de compte existe déjà.", "Memories",0x40 | 0x0)

    elif str(mdp) in open("Dare"+".txt").read():

        print("Mot de passe déjà utilisé")
        ctypes.windll.user32.MessageBoxW(None, "Ce mot de passe existe déjà.", "Memories",0x40 | 0x0)

    elif mdpv != mdp:
        print("les deux mot de passe ne correspond pas")
        ctypes.windll.user32.MessageBoxW(None, "Les deux mots de passe ne correspond pas.", "Memories",0x40 | 0x0)


    else:

        print("false")
        listelog = open("Dare"+".txt","w")
        contenuelog = contenuelog+ str(nom)+" "+str(mdp) + "\n"
        listelog.writelines(contenuelog)
        listelog.close()
        loginb.place(x=240,y=425)
        backb.place_forget()
        passw.place(x=325,y=286)
        loginframe.config(height=200)
        accountc.config(command=create_account)
        accountc.place(x=370,y=425)
        MotDePassever.place_forget()
        passwv.place_forget()
        NomDeCompte.delete(0, 'end')
        MotDePasse.delete(0, 'end')
        MotDePassever.delete(0, 'end')
        ctypes.windll.user32.MessageBoxW(None, "Votre compte a été créé.", "Memories",0x40 | 0x0)
        open('compte/' +nom,"w").close()
        os.rename('compte/'+nom,'compte/'+nom+'.dll')
        MotDePasse.config(show="*")


    os.rename("Dare.txt","Dare.dll")


def create_account():
    loginb.place_forget()
    accountc.place(x=350,y=470)
    backb.place(x=220,y=470)
    loginframe.config(height=250)
    MotDePassever.place(x=285,y=390)
    passwv.place(x=250,y=356)
    NomDeCompte.delete(0, 'end')
    MotDePasse.delete(0, 'end')
    MotDePassever.delete(0, 'end')
    accountc.config(command=create)
    MotDePasse.config(show="*")
    MotDePassever.config(show="*")
def linkstart():
    os.rename("Dare.dll","Dare.txt")
    if str(NomDeCompte.get()) == "" or str(MotDePasse.get()) == "":
    	ctypes.windll.user32.MessageBoxW(None, "Veuillez remplir les informations.", "Memories",0x40 | 0x0)
    	os.rename("Dare.txt","Dare.dll")
    elif str(NomDeCompte.get()) +" "+ str(MotDePasse.get()) in open('Dare.txt').read():
        os.rename('loginin.dll','loginin.txt')
        logh = open('loginin.txt','w')
        logh.writelines(NomDeCompte.get())
        logh.close()
        os.rename('loginin.txt','loginin.dll')
        os.startfile("DDLC.exe")
        os.rename("Dare.txt","Dare.dll")
        sys.exit("Linkstart")
    else:
        print("Compte inexistant")
        os.rename("Dare.txt","Dare.dll")


def back():
    loginb.place(x=240,y=425)
    passw.place(x=325,y=286)
    loginframe.config(height=200)
    accountc.config(command=create_account)
    accountc.place(x=370,y=425)
    MotDePassever.place_forget()
    passwv.place_forget()
    NomDeCompte.delete(0, 'end')
    MotDePasse.delete(0, 'end')
    MotDePassever.delete(0, 'end')
    MotDePasse.config(show="*")
    backb.place_forget()


log = Label(root,text="Nom du Compte",font=("Verdana",17))
log.place(x=305,y=216)
passw = Label(root,text="Mot de passe",font=("Verdana",17))
passw.place(x=325,y=286)
passwv = Label(root,text="Confirmez le mot de passe",font=("Verdana",17))

loginb = Button(root,text="Login",font=("Verdana",17),command=linkstart)

loginb.place(x=240,y=425)
backb = Button(root,text="Retour",font=("Verdana",17),command=back)
accountc = Button(root,text="Créer un compte",font=("Verdana",17),command=create_account)
accountc.place(x=370,y=425)
root.mainloop()

