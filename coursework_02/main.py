from tkinter import *
from tkinter import messagebox
import random
import time
import sys
import os

width= 1600
height= 900
# creation of main window
global mainWindow
mainWindow= Tk() #create window
mainWindow.title("Prince of The Pacific")
#Calcs computers screen size
ws= mainWindow.winfo_screenwidth()
hs= mainWindow.winfo_screenheight()
x= (ws/2) - (width/2) # calculate middle
y= (hs/2) - (hs/2)
mainWindow.geometry('%dx%d+%d+%d' % (width, height, x, y)) #window size
mainWindow.resizable(0,0)

# necessary Global variables required to read from file
global canvasGame
canvasGame= Canvas(mainWindow, width=1600, height=900, bg='black')
canvasGame.config()

score= 0

global keyChange
keyChange= True

global saveFile

global paused
paused= False

global leaderboard
leaderboard= []

global splitLdrb
splitLdrb= []

global leaderboardFile
leaderboardFile= "Leaderboard.txt"

try:
	with open(leaderboardFile) as file:
		scores= file.read()
		scores= scores.split('\n')


except:
	pass

for i in scores:
	splitLdrb.append(i.strip().split(","))
	leaderboard.append(i)


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

def leftKey1(event): #Function used to move the fish character left
	direction= "left"
	fishPos= canvasGame.coords(fish)
	if fishPos[0]>100:
		canvasGame.move(fish, -25, 0)

def rightKey1(event): #Function used to move the fish character right
	direction= "right"
	fishPos= canvasGame.coords(fish)
	if fishPos[0]<1500:
		canvasGame.move(fish, 25, 0)

def upKey1(event): #Function used to move the fish character up
	direction= "up"
	fishPos= canvasGame.coords(fish)
	if fishPos[1]>50:
		canvasGame.move(fish, 0, -25)

def downKey1(event): #Function used to move the fish character down
	direction= "down"
	fishPos= canvasGame.coords(fish)
	if fishPos[1]<850:
		canvasGame.move(fish, 0, 25)

def popupBox():
	loadgame= messagebox.askquestion(title="load game", message="Would you like to load the previously saved game?")
	if loadgame == "no":
		createGame()

	else:
		loadGame()

def createMenu(): #sets the attributes for the menu canvas
	global canvasMenu
	canvasMenu= Canvas(mainWindow, width=1600, height=900)
	canvasMenu.config(bg="black")
	canvasMenu.pack(expand= YES, fill= BOTH)
	canvasMenu.pack()

	#text used to set the name
	titleText= canvasMenu.create_text(width/2 , 30 , fill="black" , font=("Times 20 italic bold", 50) , text="Menu")

	#Necessary buttons places on the menu screen
	btnStart= Button(canvasMenu, text= "Start", bg="white", height=3, width=70, command= lambda:[canvasMenu.destroy(), popupBox()])
	btnStart.place(relx=0.5, rely=0.501, anchor=CENTER)

	btnInst= Button(canvasMenu, text= "Instructions", bg="white", height=3, width=70, command= lambda:[canvasMenu.destroy(), createInstr()])
	btnInst.place(relx=0.5, rely=0.559, anchor=CENTER)

	btnLdrb= Button(canvasMenu, text= "Leaderboard", bg="white", height=3, width=70, command= lambda:[canvasMenu.destroy(), createLdrb()])
	btnLdrb.place(relx=0.5, rely=0.617, anchor=CENTER)

	btnSet= Button(canvasMenu, text= "Settings", bg="white", height=3, width=70, command= lambda:[canvasMenu.destroy(), createSettings()])
	btnSet.place(relx=0.5, rely=0.674, anchor=CENTER)

	mainWindow.mainloop()

def createLdrb():
	# creation of leaderboard canvas
	global canvasLdrb
	canvasLdrb= Canvas(mainWindow, width=1600, height=900)
	canvasLdrb.config(bg="black")
	canvasLdrb.pack(expand= YES, fill= BOTH)
	imgbackground= PhotoImage(file= "background.png")
	canvasLdrb.create_image(800,450, image= imgbackground)
	canvasLdrb.pack()

	# necessary global variables needed for leaderboard
	global leaderboard
	leaderboard= []

	global splitLdrb
	splitLdrb= []

	global leaderboardFile
	leaderboardFile= "Leaderboard.txt"

	# reads from leaderboard file
	try:
		with open(leaderboardFile) as file:
			for line in file:
				# split each item from file
				splitLdrb.append(line.strip("\n").split(","))

		# convert the number items to integers
		for i in range(len(splitLdrb)):
			splitLdrb[i][1] = int(splitLdrb[i][1])

	except:
		pass

	# sort the leaderboard
	splitLdrb.sort(key=lambda x: x[1], reverse= True)

	print(splitLdrb)

	canvasLdrb.create_rectangle(300, 200, 1300, 700, fill= 'black')

	# creation of text for leaderboard
	ldrbTxt= canvasLdrb.create_text(width/2 , 240 , fill="white" , font=("Times 20 italic bold", 50) , text="Leaderboard:")
	ldrbFirst= canvasLdrb.create_text(width/2 , 320 , fill="white" , font=("Times 20 italic bold", 50) , text="1: " + splitLdrb[0][0] + " " + str(splitLdrb[0][1]))
	ldrbSecond= canvasLdrb.create_text(width/2 , 400 , fill="white" , font=("Times 20 italic bold", 50) , text="2: " + splitLdrb[1][0] + " " + str(splitLdrb[1][1]))
	ldrbThird= canvasLdrb.create_text(width/2 , 480 , fill="white" , font=("Times 20 italic bold", 50) , text="3: " + splitLdrb[2][0] + " " + str(splitLdrb[2][1]))
	ldrbFourth= canvasLdrb.create_text(width/2 , 560 , fill="white" , font=("Times 20 italic bold", 50) , text="4: " + splitLdrb[3][0] + " " + str(splitLdrb[3][1]))
	ldrbFifth= canvasLdrb.create_text(width/2 , 640 , fill="white" , font=("Times 20 italic bold", 50) , text="5: " + splitLdrb[4][0] + " " + str(splitLdrb[4][1]))

	# Button to return to main menu
	btnSet= Button(canvasLdrb, text= "Return", bg="black", height=3, width=20, command= lambda:[canvasLdrb.destroy(), createMenu()])
	canvasLdrb.pack()
	btnSet.place(x=10, y=800)

	mainWindow.mainloop()

def controlFalse():
	global keyChange
	keyChange= False

def controlTrue():
	global keyChange
	keyChange= True
	print("controls changed")


def createSettings():
	# creation of leaderboard canvas
	global canvasSettings
	canvasSettings= Canvas(mainWindow, width=1600, height=900)
	canvasSettings.config(bg="black")
	canvasSettings.pack(expand= YES, fill= BOTH)
	canvasSettings.pack()

	# Button to return to main menu
	btnWASD= Button(canvasSettings, text= "Use 'WASD' controls", bg="black", height=3, width=20, command= lambda:[controlTrue()])
	canvasSettings.pack()
	btnWASD.place(x=500, y=300)

	# Button to return to main menu
	btnArrows= Button(canvasSettings, text= "Use Arrow controls", bg="black", height=3, width=20, command= lambda:[controlFalse()])
	canvasSettings.pack()
	btnArrows.place(x=500, y=500)

	# Button to return to main menu
	btnSet= Button(canvasSettings, text= "Return", bg="black", height=3, width=20, command= lambda:[canvasSettings.destroy(), createMenu()])
	canvasSettings.pack()
	btnSet.place(x=10, y=800)

	mainWindow.mainloop()

def createInstr():
	# creation of leaderboard canvas
	global canvasInstr
	canvasInstr= Canvas(mainWindow, width=1600, height=900)
	canvasInstr.config(bg="black")
	canvasInstr.pack(expand= YES, fill= BOTH)
	canvasInstr.pack()

	istrText= canvasInstr.create_text(width/2 , 240 , fill="white" , font=("Times 20 italic bold", 50) , text="How to play: \n You can only eat the red fish. If you touch another colour, you die! \n Enjoy! \n (default controls: WASD")
	# Button to return to main menu
	btnSet= Button(canvasInstr, text= "Return", bg="black", height=3, width=20, command= lambda:[canvasInstr.destroy(), createMenu()])
	canvasInstr.pack()
	btnSet.place(x=10, y=800)

	mainWindow.mainloop()


def createGame(): #Function used to add the attributes for the game canvas
	global canvasGame
	canvasGame= Canvas(mainWindow, width=1600, height=900, bg='black')
	canvasGame.config()
	canvasGame.pack(expand= YES, fill= BOTH)
	canvasGame.update()
	#Create background image
	gamebg= PhotoImage(file= "game.png")
	canvasGame.create_image(800,450, image= gamebg)

	global scoreText
	scoreText= canvasGame.create_text(1500, 20, fill="black", font=("Comic Sans", 50), text="Score: " + str(score))

	#create fish character image 
	sidat= PhotoImage(file= "fish.png")
	global fish
	fish= canvasGame.create_image(90,450, image= sidat)
	canvasGame.update()
	canvasGame.config(bg="#9CEFFE")

	btn_pause= PhotoImage(file= "pause.png")
	pausebtn= Button(canvasGame, image= btn_pause, borderwidth=0, highlightthickness=0, command= pauseGame)
	pausebtn.place(x=10, y=10)

	#binds the control keys to the necessary functions for movement
	if keyChange == False:
		canvasGame.bind("<Left>", leftKey)
		canvasGame.bind("<Right>", rightKey)
		canvasGame.bind("<Up>", upKey)
		canvasGame.bind("<Down>", downKey)
	else:
		canvasGame.bind("<a>", leftKey1)
		canvasGame.bind("<d>", rightKey1)
		canvasGame.bind("<w>", upKey1)
		canvasGame.bind("<s>", downKey1)
	canvasGame.focus_set()
	canvasGame.pack()

	canvasGame.focus_set()
	canvasGame.pack()

	# Creation of necessary variables used throughout the program
	global enemyList
	enemyList= []
	global enemyPic, enemyFish
	enemyPic= []
	enemyFish = []
	global colour
	colour= ["Red", "Red", "Green", "Orange", "Pink", "Purple"]
	global enemyColour
	enemyColour= []

	while True:
		startGame()

		break


	mainWindow.mainloop()

# global fishx
fishx=1700
def createEnemy():
	global fishx
	# random colour
	f_col= random.randint(0, 5)
	# random height
	y= random.randint(50,850)
	# creation of fish pic
	fishPic= colour[f_col] + ".png"

	global enemyPicture
	enemyPicture= PhotoImage(file= fishPic)
	enemyFish.append(enemyPicture)
	enemyPic.append(fishPic)
	# place fish on canvas
	fishx= fishx+90

	enemy=(canvasGame.create_image(fishx, y, image= enemyPicture))
	enemyList.append(enemy)
	enemyColour.append(f_col)	

	# update game canvas 
	canvasGame.update()

def startGame():
	global paused
	paused = False

	# Rebind keys at when game starts
	if keyChange == False:
		canvasGame.bind("<Left>", leftKey)
		canvasGame.bind("<Right>", rightKey)
		canvasGame.bind("<Up>", upKey)
		canvasGame.bind("<Down>", downKey)
	else:
		canvasGame.bind("<A>", leftKey1)
		canvasGame.bind("<D>", rightKey1)
		canvasGame.bind("<W>", upKey1)
		canvasGame.bind("<S>", downKey1)
	canvasGame.focus_set()
	canvasGame.pack()

	while True:
		createEnemy()
		moveFish()
		if paused == True:
			#removes binds from the necessary keys
			canvasGame.unbind("<Left>")
			canvasGame.unbind("<Right>")
			canvasGame.unbind("<Up>")
			canvasGame.unbind("<Down>")
			canvasGame.focus_set()
			break

	mainWindow.mainloop()

def moveFish():
	global score
	for enemy in enemyList:

		# find position of enemy item
		pos= canvasGame.coords(enemy)
		if pos[0]>-100:
			if score<=5:
				canvasGame.move(enemy, -5, 0)

			elif score>5 and score<=10:
				canvasGame.move(enemy, -10, 0)

			elif score>10 and score<=20:
				canvasGame.move(enemy, -15, 0)

			elif score>20 and score<=30:
				canvasGame.move(enemy, -20, 0)

			elif score>30 and score<=40:
				canvasGame.move(enemy, -30, 0)

			else:
				canvasGame.move(enemy, -50, 0)

		else:
			# remove when fish is off screen
			enemyList.remove(enemy)
			canvasGame.delete(enemy)		

		# find pos of user on canvas
		fpos= canvasGame.coords(fish)
		# comparison for x position on canvas 
		if (pos[0]-47.5 <= fpos[0]+95) and (pos[0]+ 47.5 >= fpos[0]-95):

			# comparison for y position on canvas
			if(pos[1]-32.5 >= fpos[1]-65 and pos[1]+32.5<= fpos[1]+65):
				# Remove from canvas if collision
				enemyList.remove(enemy)
				canvasGame.delete(enemy)
				if enemyColour[enemy-4] == 0 or enemyColour[enemy-4] == 1 :
					# print(enemyColour[enemy])
					score= score+1
					canvasGame.itemconfig(scoreText, text="Score: " + str(score))
					print("score is:" + str(score))

				else:
					print(enemyColour[enemy-4])
					endGame()

def pauseGame():
	global paused
	paused= True
	# creation of pause window
	global pauseWindow
	pauseWindow= Tk()
	pauseWindow.title("Game Paused")
	pauseWindow.geometry('%dx%d+%d+%d' %(400, 800, 700, 75))
	pauseWindow.resizable(0,0)
	canvasPause= Canvas(pauseWindow, width=400, height=800, bg='black')

	#Necessary buttons places on the menu screen
	btnPlay= Button(canvasPause, text= "Play", bg="white", height=3, width=30, command=playGame)
	btnPlay.place(x=60, y=500)

	btnSave= Button(canvasPause, text= "Save", bg="white", height=3, width=30, command=saveGame)
	btnSave.place(x=60, y=600)
	canvasPause.pack()

	btnHome= Button(canvasPause, text= "Return to Menu", bg="white", height=3, width=30, command= lambda:[canvasGame.destroy(), pauseWindow.destroy(), createMenu()])
	btnHome.place(x=60, y=700)
	canvasPause.pack()

def playGame():
	# destroys pause window on button press
	pauseWindow.destroy()
	startGame()

def endGame():
	global paused 
	# Creation of window when game ends
	paused= True
	global endWindow
	endWindow= Tk()
	endWindow.title("Game Paused")
	# Dimentions of window
	endWindow.geometry('%dx%d+%d+%d' %(400, 800, 700, 75))
	endWindow.resizable(0,0)
	canvasEnd= Canvas(endWindow, width=400, height=800, bg="black")
	# User input for name stored on leaderboard
	global entryName
	entryName= Entry(endWindow, width= 30)
	entryName.place(x=60, y=400)
	#Necessary buttons places on the menu screen
	btnPlay= Button(canvasEnd, text= "Save to Leaderboard", bg="black", height=3, width=30, command=writeToLeaderboard)
	btnPlay.place(x=60, y=500)
	canvasEnd.pack()
	mainWindow.mainloop()

def writeToLeaderboard():
	strName= str(entryName.get())

	# Validation on name
	if len(strName)<3 or len(strName)>20:
		messagebox.showinfo("Error", "Name must be between 3 and 20 characters long")

	else:
		# adds score and name to both file and list
		savedScore= entryName.get() + "," + str(score)
		leaderboard.append(savedScore)
		leaderboardFile= open("Leaderboard.txt", "a")
		leaderboardFile.write(savedScore + "\n")
		leaderboardFile.close()
		endWindow.destroy()
		canvasGame.destroy()
		restartGame()
		createMenu()
		
		
# function to restart game
def restartGame():
	global score
	global fishx
	global paused
	# rests all variables and empties lists used
	paused= False
	print(paused)
	score= 0
	enemyList.clear()
	print (enemyList)

	enemyPic.clear()
	print(enemyPic)
	enemyColour.clear()
	print(enemyColour)

	enemyFish.clear()
	print(enemyFish)
	fishx=1700


def saveGame():
	saveFile= "Load.txt"

	# rests all variables and empties lists used
	cEnemyList= ""
	cEnemyColour= ""
	cPos=""
	fishPos= canvasGame.coords(fish)
	cFishPos= str(fishPos[0]) + "*" + str(fishPos[1])

	for i in enemyList:
		cEnemyList= cEnemyList + str(i) + " "
	
	print(cEnemyList)

	print("\n")
	
	for i in enemyColour:
		cEnemyColour= cEnemyColour + str(i) + " "
	print(cEnemyColour)
	
	for enemy in enemyList:
		pos= canvasGame.coords(enemy)
		cPos= cPos + str(pos[0]) + "*" + str(pos[1]) + " "

	print(fishx)

	with open(saveFile, 'w') as filetowrite:
		filetowrite.write(str(score) + "\n" + cEnemyList + "\n" + cEnemyColour + "\n" + cPos + "\n" + cFishPos + str(fishx))

def loadGame():
	global score
	global canvasGame
	canvasGame= Canvas(mainWindow, width=1600, height=900, bg='black')
	canvasGame.config()
	canvasGame.pack(expand= YES, fill= BOTH)
	canvasGame.update()
	#Create background image
	gamebg= PhotoImage(file= "game.png")
	canvasGame.create_image(800,450, image= gamebg)

	global scoreText
	scoreText= canvasGame.create_text(1500, 20, fill="black", font=("Comic Sans", 50), text="Score: " + str(score))

	#create fish character image 
	sidat= PhotoImage(file= "fish.png")
	global fish
	# fish= canvasGame.create_image(90,450, image= sidat)
	# canvasGame.update()
	# canvasGame.config(bg="#9CEFFE")

	btn_pause= PhotoImage(file= "pause.png")
	pausebtn= Button(canvasGame, image= btn_pause, borderwidth=0, highlightthickness=0, command= pauseGame)
	pausebtn.place(x=10, y=10)

	#binds the control keys to the necessary functions for movement
	canvasGame.bind("<Left>", leftKey)
	canvasGame.bind("<Right>", rightKey)
	canvasGame.bind("<Up>", upKey)
	canvasGame.bind("<Down>", downKey)
	canvasGame.focus_set()
	canvasGame.pack()


	
	global fishPos
	global enemyList
	enemyList= []
	global enemyPic, enemyFish
	enemyPic= []
	enemyFish = []
	global colour
	colour= ["Red", "Red", "Green", "Orange", "Pink", "Purple"]
	global enemyColour
	enemyColour= []
	# global
	global enemyPicture

	tempCoords= []
	fishCoords= []

	loadItems= []
	saveFile= "Load.txt"
	# reads from leaderboard file
	try:
		with open(saveFile) as file:
			for line in file:
				# split each item from file
				loadItems.append(line.strip("\n"))

	except:
		pass
		print("error")

	# try:
	score= int(loadItems[0])
	# enemyList= loadItems[1].split(" ")
	enemyColour= loadItems[2].split(" ")
	
	tempCoords= loadItems[3].split(" ")
	fishxy= loadItems[4].split("*")
	fishxpos= fishxy[0]
	fishypos= fishxy[1]
	fish= canvasGame.create_image(10,400, image= sidat)
	for i in range (len(tempCoords)):
		fishCoords= tempCoords[i].split("*")

		fishColour= int(enemyColour[i])
		fishPic= colour[fishColour] + ".png"
		enemyPicture= PhotoImage(file= fishPic)
		enemyFish.append(enemyPicture)
		enemyPic.append(fishPic)
		x=fishCoords[0]
		y=fishCoords[1]
		enemy= canvasGame.create_image(x, y, image= enemyPicture)
		enemyList.append(enemy)
		canvasGame.pack()
		canvasGame.update()

		while True:
			startGame()

			break

		mainWindow.mainloop()
		# except:
	# 	pass
	# 	print("error here")

# start game


createMenu()






