# Imports necessary modules
import os
import datetime
import re
import sys
from difflib import SequenceMatcher

# Function which validates inputs for a menu
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

# Boolean values for two menu for loops
valid= False
valid1=False

# Reads dictionary into the program list
englishDict_file= open("EnglishWords.txt", "r")
Dict_list= []
for line in englishDict_file:
	Dict_list.append(line.strip("\n"))
englishDict_file.close()

# Necessary variables needed for outputs
wordCount= 0
wordWrong= 0
wordRight= 0
wordAdded= 0
wordsChanged= 0
startTime= datetime.datetime.now()
checkedTime=datetime.datetime.now()

# First menu loop
while (valid== False):
	# Validates inputs for the menu
	menu = inputValidator("1- Spell check a sentence, 2- Spell check a file, 0- Quit program: \n", lim=[0,2])

	if(menu==1):
		# Collects user input for sentence
		sentence=input("Please enter a sentence: \n")
		# Removes spaces and special characters
		words= sentence.lower().strip().split(" ")
		for i in range(len(words)):
			words[i]= re.sub(r'[^a-zA-Z]+', '', words[i])
		# Original words stored by user
		originalWords= []
		for word in words:
			originalWords.append(word)

		print(originalWords)
		wordPass= True
		print(words)
		wordi=0
		# Loop through words list
		for i in words:
			print(words[wordi])
			# comparison with the word in words list with all the words in dictionary
			if (i in Dict_list):
				wordPass = True
				wordRight=wordRight+1
			else:
				wordPass = False
				wordWrong= wordWrong+1

				# Incorrect menu output
				incorrectMenu= inputValidator(words[wordi] + " spelt incorrectly, would you like to 1- Ignore, 2- Mark, 3- Add to dictionary, 4- Suggest correction\n", lim=[1,4])
				if (incorrectMenu==1):
					# increment wrong word count
					wordWrong= wordWrong+1
					pass

				elif (incorrectMenu==2):
					# Marks words, plus increment wrong word count
					words[wordi]= "?" + words[wordi] + "?"
					print("word marked incorrectly")
					wordWrong= wordWrong+1

				elif (incorrectMenu==3):
					# Adds incorrect word to the dictionary
					Dict_list.append(words[wordi])
					file= open("EnglishWords.txt", "a")
					file.write(i+"\n")
					file.close()
					wordAdded= wordAdded+1
					wordRight=wordRight+1

				elif(incorrectMenu==4):
					# Suggested correction
					score=0
					suggWord= ""
					for word in Dict_list:
						score1 = SequenceMatcher(None, word, words[wordi]).ratio()
						# Sugested correction, comparison between the scores
						if(score1> score):
							score= score1
							suggWord= word
					print("Suggested word: " + suggWord)
					# Input validator, asks user is they want to accept suggestion
					chooseWord= inputValidator("Would you like to accept the suggestion (1) or reject the suggestion (2) \n", lim=[1,2])
					if (chooseWord==1):
						words[wordi]= suggWord
						print("Word has been replaced by suggested word")
						# Increments appropriate variables
						wordsChanged= wordsChanged+1
						wordRight=wordRight+1

					if (chooseWord==2):
						print("Word marked as incorrect")
						# Increments apt variables
						wordWrong= wordWrong+1

			wordi=wordi+1
			wordCount=wordCount+1
# declare timings for the prgram
		checkedTime= datetime.datetime.now()
		elapsedTime= checkedTime-startTime
		# writes relevant info to the file
		file= open(input("please enter a file name: "), "a")
		file.write("Total words: " + str(wordCount) + " Correct words: " + str(wordRight) + " Incorrect words: " + str(wordWrong) + " Words added to dictionary: " + str(wordAdded) + " Words changed: " + str(wordsChanged)+ " Time spellchecked: " + str(checkedTime) + " elapsed time: " + str(elapsedTime) + "\n" + "Original words: ")
		for word in originalWords:
			file.write(word + " ")

		file.write("\nAmended words: ")
		for word in words:
			file.write(word + " ")
		file.close()

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
				# Removes spaces and special characters
				for i in range(len(words)):
					words[i]= re.sub(r'[^a-zA-Z]+', '', words[i])
				# Original words stored by user
				originalWords= []
				for word in words:
					originalWords.append(word)

				wordPass= True
				print(words)
				wordi=0
				# Loop through words list
				for i in words:
					print(words[wordi])
					# comparison with the word in words list with all the words in dictionary
					if (i in Dict_list):
						wordPass = True
						wordRight=wordRight+1
					else:
						wordPass = False

						incorrectMenu= inputValidator(words[wordi] + " spelt incorrectly, would you like to 1- Ignore, 2- Mark, 3- Add to dictionary, 4- Suggest correction\n", lim=[1,4])
						# Incorrect menu output
						if (incorrectMenu==1):
							wordWrong= wordWrong+1
							pass
						# Marks words, increments wrong word count
						elif (incorrectMenu==2):
							words[wordi]= "?" + words[wordi] + "?"
							print("word marked incorrectly")
							wordWrong= wordWrong+1
							print(words[wordi])
							# Adds incorrect word to the dictionary
						elif (incorrectMenu==3):
							Dict_list.append(words[wordi])
							file= open("EnglishWords.txt", "a")
							file.write(i+"\n")
							file.close()
							wordAdded= wordAdded+1
							wordRight=wordRight+1

						elif(incorrectMenu==4):
							# Suggested correction
							score=0
							suggWord= ""
							for word in Dict_list:
								score1 = SequenceMatcher(None, word, words[wordi]).ratio()
								# Sugested correction, comparison between the scores
								if(score1> score):
									score= score1
									suggWord= word
							print("Suggested word: " + suggWord)
							# Input validator, asks user is they want to accept suggestion
							chooseWord= inputValidator("Would you like to accept the suggestion (1) or reject the suggestion (2) \n", lim=[1,2])
							if (chooseWord==1):
								words[wordi]= suggWord
								print("Word has been replaced by suggested word")
								# Increments appropriate variables
								wordsChanged= wordsChanged+1
								wordRight=wordRight+1

							if (chooseWord==2):
								print("Word marked as incorrect")
								# Increments apt variables
								wordWrong= wordWrong+1

					wordi=wordi+1
					wordCount=wordCount+1
# declare timings for the prgram
				checkedTime= datetime.datetime.now()
				elapsedTime= checkedTime-startTime
				# writes relevant info to the file
				file= open(input("please enter a file name: "), "w")
				file.write("Total words: " + str(wordCount) + " Correct words: " + str(wordRight) + " Incorrect words: " + str(wordWrong) + " Words added to dictionary: " + str(wordAdded) + " Words changed: " + str(wordsChanged)+ " Time spellchecked: " + str(checkedTime) + " elapsed time: " + str(elapsedTime) + "\n" + "Original words: ")
				for word in originalWords:
					file.write(word + " ")

				file.write("\nAmended words: ")
				for word in words:
					file.write(word + " ")
				print(words)
				file.close()

				restart=inputValidator("Would you like to spellcheck a new file? Yes(1) or No (2)\n", lim=[1,2])
				if (restart==1):
					valid= False

				if(restart==2):
					valid= True



			except:
				# Invalid file name input, loops
				valid1= False
				choice=inputValidator("Invalid filename, would you like to try again (1) or return to the menu (2)\n", lim=[1,2])
				if (choice==2):
					print("")
					break


	elif(menu==0):
		# Close program
		sys.exit()
