# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''

    #convert secretWord to a list of individual charaters
    list_secretWord = list(secretWord)
    
    #creat list that tracks how many correct guess have been made
    checklist = []
    check = False
    
    #2-dimmensional iteration to check if each letter in the secret word
    # is in the list of guessed letters, is so add one "True" to the 
    # list of correct guess 'checklist'
    for i in list_secretWord:
        for j in lettersGuessed:
            if i == j:
                checklist.append(True)
                break
            
    #if the number of chars in the secret word and the number of items in the
    #checklist are the same, then the word has been guesed, retrun True
    if len(checklist) == len(list_secretWord):
        check = True
    return(check)
    

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    #defining a blank word to hold the guessed word and blank spaces
    guessedWord = ""
    
    #2-dimmensional itteration to check if each letter in the secret word is
    # included in the list of guessed words
    # if the letter in question is included int he list, then it is displayed
    # otherwise, a " _" is shown in it's place to the user
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
            

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    # start with the full string of the nower case alphabetical letters
    alphabet = string.ascii_lowercase
    
    # defining a blank string to hold the available letters in
    availableLetters = ""
    
    # iteration to check if each letter in the alphabet is contained in the 
    # lettersGuessed; if so, that letter is not included in the string of 
    # available letters
    for i in alphabet:
        if i not in lettersGuessed:
            availableLetters += i
    return(availableLetters)
    

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
            
        
        

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
