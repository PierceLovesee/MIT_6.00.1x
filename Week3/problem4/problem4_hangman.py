def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # Welcome message:
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) +" letters long.")
    print("-------------")

    # initiallizing list for keeping track of the letters guessed so far
    lettersGuessed = []

    # defining the total number of failed attempts allowed
    numGuesses = 8

    # continuous game loop
    while True:

        # case for if all letters have been guessed in the secret word (winner)
        if numGuesses > 0 and isWordGuessed(secretWord, lettersGuessed) == True:
            print("Congratulations, you won!")
            break

        # case if the number of incorrect guesses have been exceeded (game over)
        elif numGuesses < 1:
            print("Sorry, you ran out of guesses. The word was " + str(secretWord) + ".")
            break

        # base case for loop during normal game play
        else:

            # show user number of guesses remaining
            print("You have " + str(numGuesses) + " guesses left.")
            # show user available letters for guessing
            print("Available Letters: " + str(getAvailableLetters(lettersGuessed)))
            # getting user input for a letter to guess against secretWord
            guess = input("Please guess a letter: ").lower()
            # case if the letter guessed has already been guessed
            if guess in lettersGuessed:
                print("Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord, lettersGuessed)))
            # case if the letter guessed is not in the secretWord
            elif guess not in secretWord:
                lettersGuessed.append(guess)
                print("Oops! That letter is not in my word: " + str(getGuessedWord(secretWord, lettersGuessed)))
                numGuesses -= 1
            # case if the letter guessed is in the secretWord
            elif guess in secretWord:
                lettersGuessed.append(guess)
                print("Good guess: " + str(getGuessedWord(secretWord, lettersGuessed)))
            # deliniation between rounds
            print("------------")
