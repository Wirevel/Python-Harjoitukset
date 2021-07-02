import random # Adding game version 3, Save only the score

from FileReadWrite import *

DATA_FILE_PATH = 'Users/Brother/OneDrive/Documents/Textifilet code/GameData.txt'

if not fileExists(DATA_FILE_PATH): # Start up code
    score = 0
    print ('Hi, and welcome to the adding game.')
else:
    score = readFile(DATA_FILE_PATH)
    score = int(score)
    print ('Welcome back. Your saved score is:', score)
while True: # Main loop
    firstNumber = random.randrange(0, 11)
    secondNumber = random.randrange(0, 11)
    correctAnswer = firstNumber + secondNumber
    question = 'What is: ' + str(firstNumber) + ' + ' + str(secondNumber) + '? '
    userAnswer = input(question)
    if userAnswer == '':
        break

    userAnswer = int(userAnswer)

    if userAnswer == correctAnswer:
        print ('Yes, you got it!')
        score = score + 2
    else:
        print ('No, sorry, the correct answer was: ', correctAnswer)
        score = score - 1
    print ('Your current score is: ', score)
    print ()
writeFile(DATA_FILE_PATH, str(score))
print ('Thanks for playing')