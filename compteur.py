#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from tkinter import * 


<<<<<<< HEAD
=======


>>>>>>> parent of 8278f5f... dbl click pour quitter + bug retard d'une sec à la pause
fenetre = Tk()
fenetre.overrideredirect(True)
#fenetre.wm_attributes("-transparentcolor", "white")

def compte(event):
	global label
	global run
	print ("compte")
	if run == False:
		run = True
		label.after(1000,tic)
	else:
		run = False

def decompte(event):
	global label
	global run
	print ("décompte")
	if run == False:
		run = True
		label.after(1000,tac)
	else:
		run = False

def raz(event):
	global time
	global sec
	global min
	global run
	print ("clic D")
	if run == False:
	        time = 0
	        sec = 0
	        min = 0
	        run = False
	        drawTime(sec,min)

def reglage(event):
	setting = True
	

def tic():#les secondes passent, en mode chrono
#	print ("tic")
	global label
	if run == True:
		label.after(1000,tic)
	global sec
	global min
	global time
	sec += 1
#	print (sec)
<<<<<<< HEAD
		if sec > 59:
			sec = 0
			min += 1
		drawTime(sec,min)

def tac():#les secondes passent, en mode compte à rebours
#	print ("tic")
	global label
	if run == True:
		label.after(1000,tac)
		global sec
		global min
		global time
		sec -= 1
#	print (sec)
		if sec < 0:
			sec = 59
			min -= 1
		drawTime(sec,min)

def quit(self):
	exit()
=======
	if sec > 59:
		sec = 0
		min += 1
	drawTime(sec,min)
>>>>>>> parent of 8278f5f... dbl click pour quitter + bug retard d'une sec à la pause

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

min = 0
sec = 0
run = False
time = 0
setting = False
print (time)
label = Label(fenetre, text = "00:00", fg="gray", bg="white",font=("Helvetica", 90))
<<<<<<< HEAD
label.bind("<Button-1>", compte)
label.bind("<Button-3>", decompte)
label.bind("<Button-2>", reglage)
label.bind("<Double-Button-3>", raz)
label.bind("<Double-Button-1>", quit)
=======
label.bind("<Button-1>", clicG)
label.bind("<Button-3>", clicD)
>>>>>>> parent of 8278f5f... dbl click pour quitter + bug retard d'une sec à la pause
label.pack()


fenetre.mainloop()
fenetre.focus_force()
