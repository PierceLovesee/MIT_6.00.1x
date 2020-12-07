#plovesee
#September 6th, 2020
#Problem Set 1

#Assume s is a string of lower case characters.
#Write a program that counts up the number of vowels contained in the string s.
#Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example,
#if s = 'azcbobobegghakl', your program should print:
#Number of vowels: 5

#initialize vowel counter to 0
vowels = 0
# for loop to determine the number of lower case vowels in the string
for i in s:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        vowels += 1

# print out the number of vowels in the string

print("Number of vowels: " + str(vowels))
