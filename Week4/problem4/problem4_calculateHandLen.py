def calculateHandlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    lenHand = 0
    for letter in hand:
        lenHand += hand[letter]
    return lenHand
