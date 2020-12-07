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
        decryptDict = {}
        shiftDict = {}
        delinString = string.punctuation + string.digits + " "
        word = ""

        for s in range(26):
            antiShift = 26 - s
            if s == 0:
                antiShift = 0
            PlaintextMessage.change_shift(self, antiShift)
            PlaintextMessage.get_encrypting_dict(self)
            decryptText = PlaintextMessage.get_message_text_encrypted(self)
            antiShiftScore = 0
            for i in range(len(decryptText)):
                char = decryptText[i]
                if not char in delinString:
                    word += char
                if char in delinString:
                    if is_word(load_words("words.txt"), word):
                        antiShiftScore += 1
                    word = ""
            decryptDict[antiShiftScore] = decryptText
            shiftDict[antiShiftScore] = antiShift

        maxScore = max(decryptDict.keys())
        bestString = decryptDict[maxScore]
        bestAntiShift = shiftDict[maxScore]

        return (bestAntiShift, bestString)
        
