#plovesee
#September 7th, 2020
#Problem Set 1; Problem 3

Assume s is a string of lower case characters.

#Problem Statement:
#Write a program that prints the longest substring of s in which the letters
#occur in alphabetical order. For example, if s = 'azcbobobegghakl',
#then your program should print:
#Longest substring in alphabetical order is: beggh
#In the case of ties, print the first substring. For example, if s = 'abcbcd',
#then your program should print:
#Longest substring in alphabetical order is: abc

# initializing the max string to the first letter of the string
alpha_string = s[0]
max_alpha_string = alpha_string

# iterating through the string
for i in range(1, len(s)):
    # case if two letters are in alpha order
    if s[i] >= s[i-1]:
        # case if alpha string is empty; concatonate first letter
        if alpha_string == "":
            alpha_string = s[i-1]
        # concatonate additional alpha order letters
        alpha_string += s[i]
        # update max string if longer
        if len(alpha_string) > len(max_alpha_string):
            max_alpha_string = alpha_string
    # case if letters are not in alph-order
    elif s[i] < s[i-1]:
        alpha_string = ""

# print result
print("Longest substring in alphabetical order is: " + max_alpha_string)
