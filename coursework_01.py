import os
from difflib import SequenceMatcher
def inputValidator(question, lim= None):
	try:
		choice= int(input(question))
	except ValueError:
		print("Invalid Input, try again")
		return inputValidator(question, lim)
	else:
		if lim:
			if choice < lim[0] or choice > lim[1]:
				print("Invalid input, Try Again")
				return inputValidator(question, lim)
	return choice

valid= False
valid1=False

englishDict_file= open("EnglishWords.txt", "r")
Dict_list= []
for line in englishDict_file:
	Dict_list.append(line.strip("\n"))
englishDict_file.close()
# englishDict_file.readlines().strip("\n")
# print(Dict_list)

while (valid== False):
	menu = inputValidator("1- Spell check a sentence, 2- Spell check a file, 0- Quit program: \n", lim=[0,2])

	if(menu==1):
		sentence=input("Please enter a sentence: \n")
		words= sentence.lower().strip().split(" ")
		wordPass= True
		print(words)
		wordi=0
		for i in words:
			print(words[wordi])
			if (i in Dict_list):
				wordPass = True
			else:
				wordPass = False

				incorrectMenu= inputValidator(words[wordi] + " spelt incorrectly, would you like to 1- Ignore, 2- Mark, 3- Add to dictionary, 4- Suggest correction\n", lim=[1,4])
				if (incorrectMenu==1):
					pass

				elif (incorrectMenu==2):
					words[wordi]= "?" + words[wordi] + "?"
					print("word marked incorrectly")
					print(words[wordi])

				elif (incorrectMenu==3):
					Dict_list.append(words[wordi])
					file= open("EnglishWords.txt", "a")
					file.write(i+"\n")
					file.close()

				elif(incorrectMenu==4):
					score=0
					suggWord= ""
					for word in Dict_list:
						score1 = SequenceMatcher(None, word, words[wordi]).ratio()
						if(score1> score):
							score= score1
							suggWord= word
					print(suggWord)
					chooseWord= inputValidator("Would you like to accept the suggestion (1) or reject the suggestion (2) \n", lim=[1,2])

			print (wordPass)
			wordi=wordi+1

	elif(menu==2):
		while (valid1==False):
			try:
				filename= input("Please enter a file: ")
				valid= True
				valid1= True
				wordsList= []
				print("Correct file")

				with open(filename) as file:
					wordsList = file.readlines()
					print(wordsList[0:10])
			except:
				choice=inputValidator("Invalid filename, would you like to try again (1) or return to the menu (2)\n", lim=[1,2])
				if (choice==2):
					break

	elif(menu==0):
		break
