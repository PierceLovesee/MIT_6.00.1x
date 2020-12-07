import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string).
        '''
        ## defining the lowercase and uppercase strings that will be shifted
        s = string.ascii_lowercase
        S = string.ascii_uppercase

        ## empty string for storing shifted string
        shiftDict = {}

        ## loop for shifting lower case letters and adding them to the dictionary
        ## each plain text letter is the key in standard order
        ## each value is the cyphertext with the given shift
        for i in range(len(s)):
            shiftDict[s[i]] = s[(i + shift) % 26]

        ## same loop as above, but for uppercase letters
        ## the uppercase values are added on to the end of the dictionary
        ## with the lower case values at the begining
        for j in range(len(S)):
            shiftDict[S[j]] = S[(j + shift) % 26]

        return shiftDict
        

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        ## defining a string of all upper and lower case letters
        ## this will be used to check against the CHARACTERS is self.message_text
        ## to determine if that specific character needs to be shifted
        sS = string.ascii_lowercase + string.ascii_uppercase

        ## blank string for holding cyphertext
        cypherText = ""
        ## get dictionary for shifting each charater from previously defined method
        shiftDict = self.build_shift_dict(shift)

        ## iterate through given string and see if each character is to be shifted
        for i in range(len(self.message_text)):
            ## if the char in question is to be shifted, apply shift and append to cyphertext
            if self.message_text[i] in sS:
                cypherText += shiftDict[self.message_text[i]]
            ## if the char in question is not an upper or lower case letter, no shift and append
            else:
                cypherText += self.message_text[i]

        return cypherText

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        super().__init__(text)
        self.shift = shift
        
    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''

        self.encrypting_dict = self.build_shift_dict(PlaintextMessage.get_shift(self)).copy()

        return self.encrypting_dict.copy()
        
    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.apply_shift(PlaintextMessage.get_shift(self))
        
    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        super().__init__(text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        ## dictionary to hold the decoded strings (value) for each try with the associated score (key)
        decryptDict = {}
        ## dictionary to hold the shift applied (value) for each try with the associated score (key)
        shiftDict = {}
        ## string defined to break up the decoded string and check each word
        delinString = string.punctuation + string.digits + " "
        ## variable for holding a word to check if its valid; reset after each char in delinString
        word = ""

        ## iterates through every possible shift
        for s in range(26):
            ## defines the antishift to be applied
            antiShift = 26 - s
            ## makes the antiShift 0 instead of 26 for no shift
            if s == 0:
                antiShift = 0
            ## changes the shift being applied to the antiShift
            PlaintextMessage.change_shift(self, antiShift)
            ## redefines the encryption dictionary using the antiShift
            PlaintextMessage.get_encrypting_dict(self)
            ## variable to hold the text with the antiShit trial applied
            decryptText = PlaintextMessage.get_message_text_encrypted(self)
            ## variable to hold the trials score (number of valid words)
            antiShiftScore = 0

            ## iterate through the string with the antishift applied
            ## chicking to see how many words are valid
            for i in range(len(decryptText)):
                ## looking at each character in the string and determining if
                ## it's the end of a word or not
                char = decryptText[i]
                if not char in delinString:
                    word += char
                if char in delinString:
                    ## incrimenting the antiShiftScore if the word is a valid word
                    if is_word(load_words("words.txt"), word):
                        antiShiftScore += 1
                    ## reseting the word to a blank string for next word
                    word = ""

            ## recording both the string and the antiShift with the score for each round
            decryptDict[antiShiftScore] = decryptText
            shiftDict[antiShiftScore] = antiShift

        ## once each possible antiShift is tried; find the antiShift and associated
        ## decoded string with the best score; return them as a tuple
        maxScore = max(decryptDict.keys())
        bestString = decryptDict[maxScore]
        bestAntiShift = shiftDict[maxScore]
        
        return (bestAntiShift, bestString)                    
        
#Example test case (PlaintextMessage)
plaintext = PlaintextMessage('hello', 2)
print('Expected Output: jgnnq')
print('Actual Output:', plaintext.get_message_text_encrypted())
    
#Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('jgnnq')
print('Expected Output:', (24, 'hello'))
print('Actual Output:', ciphertext.decrypt_message())

def decrypt_story():
    s = get_story_string()
    story = CiphertextMessage(s)
    return story.decrypt_message()

decrypt_story()
