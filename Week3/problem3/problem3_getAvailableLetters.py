def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabet = string.ascii_lowercase
    availableLetters = ""
    for i in alphabet:
        if i not in lettersGuessed:
            availableLetters += i
    return(availableLetters)

    
