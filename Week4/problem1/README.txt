Problem 1 - Word Scores
10.0/10.0 points (graded)
The first step is to implement some code that allows us to calculate the score
for a single word. The function getWordScore should accept as input a string of
lowercase letters (a word) and return the integer score for that word, using
the game's scoring rules.

A Reminder of the Scoring Rules

Hints:
You may assume that the input word is always either a string of lowercase
letters, or the empty string "".

You will want to use the SCRABBLE_LETTER_VALUES dictionary defined at the top
of ps4a.py. You should not change its value.

Do not assume that there are always 7 letters in a hand! The parameter n is the
number of letters required for a bonus score (the maximum number of letters in
the hand). Our goal is to keep the code modular - if you want to try playing
your word game with n=10 or n=4, you will be able to do it by simply changing
the value of HAND_SIZE!

Testing: If this function is implemented properly, and you run test_ps4a.py,
you should see that the test_getWordScore() tests pass. Also test your
implementation of getWordScore, using some reasonable English words.

Fill in the code for getWordScore in ps4a.py and be sure you've passed the
appropriate tests in test_ps4a.py before pasting your function definition here.
