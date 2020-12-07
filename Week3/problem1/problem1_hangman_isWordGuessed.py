def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...

    list_secretWord = list(secretWord)
    checklist = []
    check = False

    for i in list_secretWord:
        for j in lettersGuessed:
            if i == j:
                checklist.append(True)
                break
    if len(checklist) == len(list_secretWord):
        check = True
    return(check)
    
