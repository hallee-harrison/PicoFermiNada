print("Pico, Fermi, Nada Logic Game")
print("Instructions:")
print("You are trying to guess the random computer generated mystery number.")
print("You will begin by guessing a 3 digit number. You will be given clues based upon the number you guess.")
print("N = Nada: no digits are in the mystery number")
print("F = Fermi: you have a correct digit in the correct place value")
print("P = Pico: you have a correct digit, but not in the correct place value")

playAgain = 'p'
userGuessList = []

#define main game function
def main():
    #import random 3 digit number
    import random

    hundredsDigit = str(random.randint(0, 9))
    tensDigit = str(random.randint(0, 9))
    onesDigit = str(random.randint(0, 9))

    #string together each place value to make 3 digit number - I DON'T THINK THIS IS NEEDED
    mysteryNumber = hundredsDigit + tensDigit + onesDigit
    #print random mysteryNumber - this is only for creating purposes, needs to be removed once complete
    #print(mysteryNumber)

    #Put mystery numbers in a list
    mysteryNumberList = [hundredsDigit, tensDigit, onesDigit]



    #get user guess function
    def userGuess():
        userNumberInput = str(input("Guess a 3 digit number: "))
        userNumberList = [str(i) for i in userNumberInput]
        acceptableDigitList = ['0','1','2','3','4','5','6','7','8','9']

        while len(userNumberList) != 3 or userNumberList[0] not in acceptableDigitList or userNumberList[1] not in acceptableDigitList or userNumberList[2] not in acceptableDigitList:
            if len(userNumberList) != 3:
                print("Guess needs to be a 3 digit number.")
                userNumberInput = str(input("Guess a 3 digit number? "))
                userNumberList = [str(i) for i in userNumberInput]
            else:
                userNumberInput = str(input("Please guess a number using 3 digits: "))
                userNumberList = [str(i) for i in userNumberInput]

        #userGuessList.append(userNumberInput)
        #numberElementsUserGuessList = len(userGuessList)
        #print(userGuessList)
        #print(numberElementsUserGuessList)
        userGuessCount()
        return userNumberList

    userNumberList = userGuess()

    #function to count the number of guesses
    def userGuessCount():
        userGuessList.append(userNumberList)
        numberElementsUserGuessList = len(userGuessList)
        return numberElementsUserGuessList

    numberElementsUserGuessList = userGuessCount()


    #check user guess against mystery number
    def placeValueCheck():
        def hundredsPlaceCheck():
            if userNumberList[0] in mysteryNumberList:
                if userNumberList[0] == mysteryNumberList[0]:
                    hundredsCheck = "F"
                    return hundredsCheck
                if mysteryNumberList[0] == userNumberList[1] or mysteryNumberList[0] == userNumberList[2]:
                    hundredsCheck="P"
                    return hundredsCheck

        def tensPlaceCheck():
            if userNumberList[1] in mysteryNumberList:
                if userNumberList[1] == mysteryNumberList[1]:
                    tensCheck = "F"
                    return tensCheck
                if mysteryNumberList[1] == userNumberList[0] or mysteryNumberList[1] == userNumberList[2]:
                    tensCheck = "P"
                    return tensCheck

        def onesPlaceCheck():
            if userNumberList[2] in mysteryNumberList:
                if userNumberList[2] == mysteryNumberList[2]:
                    onesCheck = "F"
                    return onesCheck
                if mysteryNumberList[2] == userNumberList[0] or mysteryNumberList[2] == userNumberList[1]:
                    onesCheck = "P"
                    return onesCheck

        hundredsCheck = hundredsPlaceCheck()
        tensCheck = tensPlaceCheck()
        onesCheck = onesPlaceCheck()

        hundredsPlaceCheck()
        tensPlaceCheck()
        onesPlaceCheck()

        returnResponse = [hundredsCheck, tensCheck, onesCheck]
        removeNoneResponse = list(filter(None, returnResponse))
        sortedResponse = sorted(removeNoneResponse)
        returnResponse = "".join(sortedResponse)

        return returnResponse

    #when user number does not match the mystery number exactly
    while userNumberList != mysteryNumberList:
        if userNumberList[0] not in mysteryNumberList and userNumberList[1] not in mysteryNumberList and userNumberList[2] not in mysteryNumberList:
            print("N")
        else:
            returnResponse = placeValueCheck()
            placeValueCheck()
            print(returnResponse)

        userNumberList = userGuess()

    #when user correctly guesses the number
    if userNumberList == mysteryNumberList:
        print("Nice job! You correctly guessed the number, " + mysteryNumber + "!")
        print("It took you, " + str(numberElementsUserGuessList) + "guesses.")
        playAgain = input("Press 'p' to play again. Press any other key to exit. ")
        if playAgain.lower() != "p":
            quit()

while playAgain == "p":
    main()