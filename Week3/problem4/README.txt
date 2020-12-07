Problem 4
1.0/1 point (ungraded)
Now you will implement the function hangman, which takes one parameter - the
secretWord the user is to guess. This starts up an interactive game of Hangman
between the user and the computer. Be sure you take advantage of the three helper
functions, isWordGuessed, getGuessedWord, and getAvailableLetters, that you've
defined in the previous part.

Hints:
You should start by noticing where we're using the provided functions (at the
top of ps3_hangman.py) to load the words and pick a random one. Note that the
functions loadWords and chooseWord should only be used on your local machine,
not in the tutor. When you enter in your solution in the tutor, you only need
to give your hangman function.

Consider using lower() to convert user input to lower case. For example:

guess = 'A'
guessInLowerCase = guess.lower()
Consider writing additional helper functions if you need them!

There are four important pieces of information you may wish to store:

secretWord: The word to guess.
lettersGuessed: The letters that have been guessed so far.
mistakesMade: The number of incorrect guesses made so far.
availableLetters: The letters that may still be guessed. Every time a player
guesses a letter, the guessed letter must be removed from availableLetters
(and if they guess a letter that is not in availableLetters, you should print
a message telling them they've already guessed that - so try again!).

Sample Output
The output of a winning game should look like this...
And the output of a losing game should look like this...

Note that if you choose to use the helper functions isWordGuessed,
getGuessedWord, or getAvailableLetters, you do not need to paste your
definitions in the box. We have supplied our implementations of these functions
for your use in this part of the problem. If you use additional helper
functions, you will need to paste those definitions here.

Your function should include calls to input to get the user's guess.
