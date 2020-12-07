from tkinter import *
import random
import time

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

# Creation of canvases
canvasMenu= Canvas(mainWindow, width=1600, height=900)
canvasGame= Canvas(mainWindow, width=1600, height=900, bd=0)



def leftKey(event): #Function used to move the fish character left
	direction= "left"
	fishPos= canvasGame.coords(fish)
	if fishPos[0]>100:
		canvasGame.move(fish, -25, 0)

def rightKey(event): #Function used to move the fish character right
	direction= "right"
	fishPos= canvasGame.coords(fish)
	if fishPos[0]<1500:
		canvasGame.move(fish, 25, 0)

def upKey(event): #Function used to move the fish character up
	direction= "up"
	fishPos= canvasGame.coords(fish)
	if fishPos[1]>50:
		canvasGame.move(fish, 0, -25)

def downKey(event): #Function used to move the fish character down
	direction= "down"
	fishPos= canvasGame.coords(fish)
	if fishPos[1]<850:
		canvasGame.move(fish, 0, 25)


def createMenu(): #sets the attributes for the menu canvas
	
	canvasMenu.config(bg="#9CEFFE")
	canvasMenu.pack(expand= YES, fill= BOTH)
	imgbackground= PhotoImage(file= "background.png")
	canvasMenu.create_image(800,450, image= imgbackground)
	canvasMenu.pack()

	#tesxt used to set the name
	Titletext= canvasMenu.create_text(width/2 , 30 , fill="black" , font=("Times 20 italic bold", 50) , text="Menu")

	#Necessary buttons places on the menu screen
	btnStart= Button(canvasMenu, text= "Start", bg="white", height=3, width=70, command= lambda:[canvasMenu.destroy(), createGame()])
	btnStart.place(relx=0.5, rely=0.501, anchor=CENTER)

	btnInst= Button(canvasMenu, text= "Instructions", bg="white", height=3, width=70)
	btnInst.place(relx=0.5, rely=0.559, anchor=CENTER)

	btnLdrb= Button(canvasMenu, text= "Leaderboard", bg="white", height=3, width=70)
	btnLdrb.place(relx=0.5, rely=0.617, anchor=CENTER)

	btnSet= Button(canvasMenu, text= "Settings", bg="white", height=3, width=70)
	btnSet.place(relx=0.5, rely=0.674, anchor=CENTER)

	mainWindow.mainloop()

def createGame(): #Function used to add the attributes for the game canvas
	canvasGame.config()
	canvasGame.pack(expand= YES, fill= BOTH)
	#Create background image
	gamebg= PhotoImage(file= "game.png")
	canvasGame.create_image(800,450, image= gamebg)

	#create fish character image 
	sidat= PhotoImage(file="fish.png")
	global fish
	fish=canvasGame.create_image(90,450, image= sidat)
	canvasGame.config(bg="#9CEFFE")

	#binds the control keys to the necessary functions for movement
	canvasGame.bind("<Left>", leftKey)
	canvasGame.bind("<Right>", rightKey)
	canvasGame.bind("<Up>", upKey)
	canvasGame.bind("<Down>", downKey)
	canvasGame.focus_set()

	# Creation of necessary variables used throughout the program
	global enemyList
	enemyList= []
	global enemyPic, fishes
	enemyPic= []
	fishes = []
	global colour
	colour= ["Red", "Red", "Green", "Orange", "Pink", "Purple"]
	global enemyColour
	enemyColour= []
	while True:

		delayFish()

		# print(enemyPic)
		break


	mainWindow.mainloop()

def createEnemy():
	for i in range (3):
		# random colour
		f_col= random.randint(0, 5)
		# random height
		y= random.randint(0,900)
		# creation of fish pic
		fishPic= colour[f_col] + ".png"
		enemyPicture= PhotoImage(file= fishPic)
		fishes.append(enemyPicture)
		enemyPic.append(fishPic)
		# place fish on canvas
		enemy=(canvasGame.create_image(800, y, image= enemyPicture))
		enemyList.append(enemy)
		# update game canvas 
		canvasGame.update()
		

def delayFish():
	createEnemy()
	print (enemyList)
	for enemy in enemyList:
		pos= canvasGame.coords(enemy)
		print(pos)
		if pos[0]>0:
			canvasGame.move(enemy, -100, 0)
			print(pos)

	mainWindow.after(3000, delayFish)



createMenu()






