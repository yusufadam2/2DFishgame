from tkinter import *
import random

width= 1600
height= 900
global mainWindow
mainWindow= Tk() #create window
mainWindow.title("Prince of The Pacific")
#Calcs computers screen size
ws= mainWindow.winfo_screenwidth()
hs= mainWindow.winfo_screenheight()
x= (ws/2) - (width/2) # calculate middle
y= (hs/2) - (hs/2)
mainWindow.geometry('%dx%d+%d+%d' % (width, height, x, y)) #window size

canvasMenu= Canvas(mainWindow, width=1600, height=900)

def createMenu():
	
	canvasMenu.config(bg="#9CEFFE")
	canvasMenu.pack(expand= YES, fill= BOTH)
	imgbackground= PhotoImage(file= "background.png")
	canvasMenu.create_image(800,450, image= imgbackground)
	canvasMenu.pack()

	Titletext= canvasMenu.create_text(width/2 , 30 , fill="black" , font=("Times 20 italic bold", 50) , text="Menu")

	btnStart= Button(mainWindow, text= "Start", bg="white", height=3, width=70, command= createGame)
	btnStart.place(relx=0.5, rely=0.5, anchor=CENTER)

	btnInst= Button(mainWindow, text= "Instructions", bg="white", height=3, width=70)
	btnInst.place(relx=0.5, rely=0.559, anchor=CENTER)

	btnLdrb= Button(mainWindow, text= "Leaderboard", bg="white", height=3, width=70)
	btnLdrb.place(relx=0.5, rely=0.617, anchor=CENTER)

	btnSet= Button(mainWindow, text= "Settings", bg="white", height=3, width=70)
	btnSet.place(relx=0.5, rely=0.674, anchor=CENTER)

	mainWindow.mainloop()

def createGame():

	def leftKey(event):
		direction= "left"
		fishPos= canvasGame.coords(fish)
		if fishPos[0]>100:
			canvasGame.move(fish, -20, 0)

	def rightKey(event):
		direction= "right"
		fishPos= canvasGame.coords(fish)
		if fishPos[0]<1500:
			canvasGame.move(fish, 20, 0)

	def upKey(event):
		direction= "up"
		fishPos= canvasGame.coords(fish)
		if fishPos[1]>50:
			canvasGame.move(fish, 0, -20)

	def downKey(event):
		direction= "down"
		fishPos= canvasGame.coords(fish)
		if fishPos[1]<850:
			canvasGame.move(fish, 0, 20)

	print("hello")
	width= 1600
	height= 900
	canvasMenu.destroy()

	canvasGame= Canvas(mainWindow, width=1600, height=900, bd=0)
	canvasGame.pack(expand= YES, fill= BOTH)
	gamebg= PhotoImage(file= "game.png")
	canvasGame.create_image(800,450, image= gamebg)

	sidat= PhotoImage(file="fish.png")
	fish=canvasGame.create_image(90,450, image=sidat)
	canvasGame.config(bg="#9CEFFE")

	canvasGame.bind("<Left>", leftKey)
	canvasGame.bind("<Right>", rightKey)
	canvasGame.bind("<Up>", upKey)
	canvasGame.bind("<Down>", downKey)
	canvasGame.focus_set()

	

	mainWindow.mainloop()

createMenu()









