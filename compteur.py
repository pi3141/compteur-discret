#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import * 

#variable config
OPACITE = 0.9 #de 0 à 1


fenetre = Tk()
fenetre.overrideredirect(True)
#fenetre.wm_attributes("-transparentcolor", "white")

screenWidth = ( fenetre.winfo_screenwidth() - 330 )

fenetre.geometry("330x180+"+ str(screenWidth) + "+0")


#transparence sous linux
fenetre.wait_visibility(fenetre)
fenetre.wm_attributes('-alpha',OPACITE)

def departStop(event):
    global label,run,setting,fini
    if fini == True:
        label.config(bg="light gray")
        fini = False
        return
    print ("departStop")
    if run == False:
        label.after(1000,tic)
        run = True
        label.config(fg="dark slate gray")
    else:
        run = False
        label.config(fg="light slate gray")
    if setting == True:
        reglage()

def raz(event):
    global time,sec,min,run,setting
    print ("raz")
    if run == False:
            time = 0
            sec = 0
            min = 0
            run = False
            drawTime(sec,min)
    if setting == True:
        reglage()

def reglage(*event):
    global label,setting
    print ("reglage")
    run = False
    if setting == False:
        setting = True
    else:
        setting = False
    if setting == True:
        label.config(fg="spring green 4")
    else:
        setting = False
        label.config(fg="light slate gray")
    
def alterne(event=""):
        global chrono,setting,separateur
        if chrono == True:
                chrono = False
                separateur.config(bg="firebrick")
        else:
                chrono = True
                separateur.config(bg="dark turquoise")
        if setting == True:
          reglage()

def tic():#les secondes passent
    global chrono
    global label
    if run == True and setting == False:
        global sec
        global min
        global time
        if chrono == True:
            label.after(1000,tic)
            sec += 1
            if sec > 59:
                    sec = 0
                    min += 1
            drawTime(sec,min)
        else:
            label.after(1000,tic)
            sec -= 1
            if sec < 0:
                if min > 0:
                    sec = 59
                    min -= 1
                else:
                    sec += 1
                    timeIsUp()
            drawTime(sec,min)

def quit(self):
    sys.exit()

def timeIsUp():
    global label,fenetre,run,fini,chrono,separateur
    run = False
    label.config(bg="red")
    fini = True
    chrono = True
    separateur.config(bg="dark turquoise")

def drawTime(sec,min):
    global time
    global label
    if min < 10:
        strmin = "0" + str(min)
    else:
        strmin = str(min)
    
    if sec < 10:
        strsec = "0" + str(sec)
    else:
        strsec = str(sec)
    time = (strmin + ":" + strsec)
    label.config(text=time)
    
def mouse_wheel(event):
    print ("mouse_wheel")
    if setting == True:
        global min,sec
        # respond to Linux or Windows wheel event
        if event.num == 5 or event.delta == -120:
            min -= 1
        if event.num == 4 or event.delta == 120:
            min += 1
    drawTime(sec,min)


min = 0
sec = 0
run = False
time = 0
chrono = True
setting = False
count = 0
fini = False

print (time)
label = Label(fenetre, text = "00:00", fg="light slate gray", font=("Helvetica", 90))

label.bind("<Button-1>", departStop)
label.bind("<Double-Button-1>", reglage)
label.bind("<Button-3>", raz)
label.bind("<Double-Button-3>", quit)
label.bind("<Button-2>", alterne)

# with Windows OS
fenetre.bind("<MouseWheel>", mouse_wheel)
# with Linux OS
fenetre.bind("<Button-4>", mouse_wheel)
fenetre.bind("<Button-5>", mouse_wheel)

separateur = Frame(height=2, bd=1, bg="dark turquoise")
separateur.pack(fill=X, padx=5, pady=5)

label.pack()

fenetre.mainloop()
fenetre.focus_force()


