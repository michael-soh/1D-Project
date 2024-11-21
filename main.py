import random


# list = ["cake", "miss", "crew"]
list = ["miss", "miss", "miss"]
# can use dictionary to tie word to hints
successletters ={}
print("Game Start")
seed = random.randint(0, 2)
word = list[seed]
print(word)

checkWord = [letter for letter in word]
# letters in the given word
def initialiseDict(checkword):
    for i in range(len(checkword)):
        # print(i)
        successletters[i] = {i: False}

initialiseDict(checkWord)
print(successletters.values())

print(successletters.keys())
def main():
    guessLetter = input("Guess a letter!")
    startGame(guessLetter, checkWord)
def startGame(guessLetter,checkWord):
    checkFunction(guessLetter, checkWord)
    if checkFunction(guessLetter,checkWord) == True:
        print("Good Job")
        print(successletters.values())
        falseExists = successletters.values()
        print(False in falseExists)
        if False in falseExists:
            main()
        # elif (for i in range(len(falseExists))):

            print("Game End")
    else:
        print("Try Again")
        main()
# def getUserInput():
#     guessLetter = input("Guess a letter!")
#     return guessLetter
def checkFunction(guessLetter, checkWord):
    # print(checkWord)
    flag = False
    for i in range(len(checkWord)):
        # print(checkWord[i])
        if (checkWord[i] == guessLetter):
            # guess S is = letter given S
            print(successletters[i])
            updateDict(i)
            flag = True
            continue
    if flag is False:
        return False
    else:
        return True

def updateDict(checkWord):
    # print(checkWord)
    # update letter to true after correct guess
    successletters[checkWord] = {checkWord: True}

# //TODO FIX CAPITALISATION NOT RECOGNIZING


main()
