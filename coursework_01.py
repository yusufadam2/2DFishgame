import os
import datetime
import re
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

wordCount= 0
wordWrong= 0
wordRight= 0
wordAdded= 0
wordsChanged= 0
startTime= datetime.datetime.now()
checkedTime=datetime.datetime.now()

while (valid== False):
	menu = inputValidator("1- Spell check a sentence, 2- Spell check a file, 0- Quit program: \n", lim=[0,2])

	if(menu==1):
		sentence=input("Please enter a sentence: \n")
		words= sentence.lower().strip().split(" ")
		for i in range(len(words)):
			words[i]= re.sub(r'[^a-zA-Z]+', '', words[i])

		originalWords= words
		wordPass= True
		print(words)
		wordi=0
		for i in words:
			print(words[wordi])
			if (i in Dict_list):
				wordPass = True
				wordRight=wordRight+1
			else:
				wordPass = False
				wordWrong= wordWrong+1

				incorrectMenu= inputValidator(words[wordi] + " spelt incorrectly, would you like to 1- Ignore, 2- Mark, 3- Add to dictionary, 4- Suggest correction\n", lim=[1,4])
				if (incorrectMenu==1):
					wordWrong= wordWrong+1
					pass

				elif (incorrectMenu==2):
					words[wordi]= "?" + words[wordi] + "?"
					print("word marked incorrectly")
					wordWrong= wordWrong+1
					print(words[wordi])

				elif (incorrectMenu==3):
					Dict_list.append(words[wordi])
					file= open("EnglishWords.txt", "a")
					file.write(i+"\n")
					file.close()
					wordAdded= wordAdded+1
					wordRight=wordRight+1

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
					if (chooseWord==1):
						words[wordi]= suggWord
						print("Word has been replaced by suggested word")
						wordsChanged= wordsChanged+1
						wordRight=wordRight+1

					if (chooseWord==2):
						print("Word marked as incorrect")
						wordWrong= wordWrong+1


			print (wordPass)
			wordi=wordi+1
			wordCount=wordCount+1

		checkedTime= datetime.datetime.now()
		print(startTime)
		print(checkedTime)
		elapsedTime= checkedTime-startTime
		print(elapsedTime)
		file= open(input("please enter a file name: "), "w")
		file.write("Total words: " + str(wordCount) + " Correct words: " + str(wordRight) + " Incorrect words: " + str(wordWrong) + " Words added to dictionary: " + str(wordAdded) + " Words changed: " + str(wordsChanged)+ " Time spellchecked: " + str(checkedTime) + " elapsed time: " + str(elapsedTime) + "\n" + "Original words: ")
		for word in originalWords:
			file.write(word + " ")

		restart=inputValidator("Would you like to spellcheck a new file? Yes(1) or No (2)\n", lim=[1,2])
		if (restart==1):
			valid= False

		if(restart==2):
			valid= True

	elif(menu==2):
		while (valid1==False):
			try:
				filename= input("Please enter a file: ")
				valid1= True
				words= []
				print("Correct file")

				with open(filename) as file:
					words= file.read()
					words=words.split(" ")
					print(words)

				# words= wordsList.lower().strip().split(" ")
				# for i in wordsList:
				# 	words= wordsList[i] + " "

				# print (words)

				for i in range(len(words)):
					words[i]= re.sub(r'[^a-zA-Z]+', '', words[i])
					print(words[i])

				originalWords= words
				wordPass= True
				print(words)
				wordi=0
				for i in words:
					print(words[wordi])
					if (i in Dict_list):
						wordPass = True
						wordRight=wordRight+1
					else:
						wordPass = False

						incorrectMenu= inputValidator(words[wordi] + " spelt incorrectly, would you like to 1- Ignore, 2- Mark, 3- Add to dictionary, 4- Suggest correction\n", lim=[1,4])
						if (incorrectMenu==1):
							wordWrong= wordWrong+1
							pass

						elif (incorrectMenu==2):
							words[wordi]= "?" + words[wordi] + "?"
							print("word marked incorrectly")
							wordWrong= wordWrong+1
							print(words[wordi])

						elif (incorrectMenu==3):
							Dict_list.append(words[wordi])
							file= open("EnglishWords.txt", "a")
							file.write(i+"\n")
							file.close()
							wordAdded= wordAdded+1
							wordRight=wordRight+1

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
							if (chooseWord==1):
								words[wordi]= suggWord
								print("Word has been replaced by suggested word")
								wordsChanged= wordsChanged+1
								wordRight=wordRight+1

							if (chooseWord==2):
								print("Word marked as incorrect")
								wordWrong= wordWrong+1

					wordi=wordi+1
					wordCount=wordCount+1

				checkedTime= datetime.datetime.now()
				print(startTime)
				print(checkedTime)
				elapsedTime= checkedTime-startTime
				print(elapsedTime)
				file= open(input("please enter a file name: "), "w")
				file.write("Total words: " + str(wordCount) + " Correct words: " + str(wordRight) + " Incorrect words: " + str(wordWrong) + " Words added to dictionary: " + str(wordAdded) + " Words changed: " + str(wordsChanged)+ " Time spellchecked: " + str(checkedTime) + " elapsed time: " + str(elapsedTime) + "\n" + "Original words: ")
				for word in originalWords:
					file.write(word + " ")

				restart=inputValidator("Would you like to spellcheck a new file? Yes(1) or No (2)\n", lim=[1,2])
				if (restart==1):
					valid= False

				if(restart==2):
					valid= True



			except:
				valid1= False
				choice=inputValidator("Invalid filename, would you like to try again (1) or return to the menu (2)\n", lim=[1,2])
				if (choice==2):
					print("")
					break


	elif(menu==0):
		sys.exit()
