def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...

    guessedWord = ""
    for i in list(secretWord):
        correctGuess = False
        for j in lettersGuessed:
            if i == j:
                correctGuess = True
                break
        if correctGuess == True:
            guessedWord += i
        else:
            guessedWord += "_ "
    return(guessedWord)
