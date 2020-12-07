def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function


    ## boolean switch for tracking state through out function
    result = False

    ## check to see if word is actually a word
    if word in wordList:
        result = True
    else:
        return False

    ## check to see if all letters are in hand
    ## also check the number of letters in hand is not exceeded
    wordDict = getFrequencyDict(word)

    for letter in wordDict:
        if letter not in hand:
            return False
        if wordDict[letter] > hand[letter]:
            return False

    return result
    
