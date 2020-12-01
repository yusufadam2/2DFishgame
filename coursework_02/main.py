from tkinter import *
import random

def setWindowDimensions(w,h):
	window= Tk() #create window
	window.title("Prince of The Pacific")
	#Calcs computers screen size
	ws= window.winfo_screenwidth()
	hs= window.winfo_screenheight()
	x= (ws/2) - (w/2) # calculate middle
	y= (hs/2) - (hs/2)
	window.geometry('%dx%d+%d+%d' % (w, h, x, y)) #window size
	
	return window

def createMenu():
	width= 1600
	height= 900
	menuWindow= setWindowDimensions(width, height)

	imgbackground=PhotoImage(file= "background.png")

	canvas= Canvas(menuWindow, width=1600, height=900)
	canvas.pack(expand= YES, fill= BOTH)
	canvas.create_image(800,450, image= imgbackground)
	canvas.config(bg="#9CEFFE")

	Titletext= canvas.create_text(width/2 , 30 , fill="black" , font=("Times 20 italic bold", 50) , text="Menu")

	btnStart= Button(menuWindow, text= "Start", bg="white", height=3, width=70)
	btnStart.place(relx=0.5, rely=0.5, anchor=CENTER)

	btnInst= Button(menuWindow, text= "Instructions", bg="white", height=3, width=70)
	btnInst.place(relx=0.5, rely=0.558, anchor=CENTER)

	btnLdrb= Button(menuWindow, text= "Leaderboard", bg="white", height=3, width=70)
	btnLdrb.place(relx=0.5, rely=0.616, anchor=CENTER)

	btnSet= Button(menuWindow, text= "Settings", bg="white", height=3, width=70)
	btnSet.place(relx=0.5, rely=0.673, anchor=CENTER)

	menuWindow.mainloop()

createMenu()