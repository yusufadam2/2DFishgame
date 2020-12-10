from tkinter import *
from tkinter import messagebox
import random
import time

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

# necessary Global variables 
score= 0

global paused
paused= False

global leaderboard
leaderboard= []

global leaderboardFile
leaderboardFile= "Leaderboard.txt"

scores= []
try:
	with open(leaderboardFile) as file:
		scores= file.read()
		scores= scores.split("\n")

except:
	pass

for i in scores:
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


def createMenu(): #sets the attributes for the menu canvas
	global canvasMenu
	canvasMenu= Canvas(mainWindow, width=1600, height=900)
	canvasMenu.config(bg="black")
	canvasMenu.pack(expand= YES, fill= BOTH)
	imgbackground= PhotoImage(file= "background.png")
	canvasMenu.create_image(800,450, image= imgbackground)
	canvasMenu.pack()

	#text used to set the name
	titleText= canvasMenu.create_text(width/2 , 30 , fill="black" , font=("Times 20 italic bold", 50) , text="Menu")

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
	canvasGame.bind("<Left>", leftKey)
	canvasGame.bind("<Right>", rightKey)
	canvasGame.bind("<Up>", upKey)
	canvasGame.bind("<Down>", downKey)
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
	
	enemyPicture= PhotoImage(file= fishPic)
	enemyFish.append(enemyPicture)
	enemyPic.append(fishPic)
	# place fish on canvas
	fishx= fishx+100

	enemy=(canvasGame.create_image(fishx, y, image= enemyPicture))
	enemyList.append(enemy)
	enemyColour.append(f_col)	

	# update game canvas 
	canvasGame.update()

def startGame():
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
			print("pause works")
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

			else:
				canvasGame.move(enemy, -20, 0)

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
					endGame()

def pauseGame():
	
	paused= True
	# creation of pause window
	global pauseWindow
	pauseWindow= Tk()
	pauseWindow.title("Game Paused")
	pauseWindow.geometry('%dx%d+%d+%d' %(400, 800, 700, 75))
	pauseWindow.resizable(0,0)
	canvasPause= Canvas(pauseWindow, width=400, height=800)

	#Necessary buttons places on the menu screen
	btnPlay= Button(canvasPause, text= "Play", bg="black", height=3, width=30, command=playGame)
	btnPlay.place(x=60, y=500)
	canvasPause.pack()


def playGame():
	# destroys pause window on button press
	pauseWindow.destroy()
	startGame()

def endGame():
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
		savedScore= entryName.get() + " " + str(score)
		leaderboard.append(savedScore)
		leaderboardFile= open("Leaderboard.txt", "a")
		leaderboardFile.write(savedScore + "\n")
		leaderboardFile.close()
		endWindow.destroy()
		canvasGame.destroy()
		restartGame()
		createMenu()
		
		

def restartGame():
	global score
	global fishx

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

createMenu()






