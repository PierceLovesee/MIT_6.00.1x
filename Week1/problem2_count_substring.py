#plovesee
#September 6th, 2020
#Problem Set 1; Problem 2

# Problem Statement:
#Assume s is a string of lower case characters.
#Write a program that prints the number of times the string 'bob' occurs in s.
#For example, if s = 'azcbobobegghakl', then your program should print
#Number of times bob occurs is: 2

#defining the substring and intializing bob_count to 0
sb = 'bob'
bob_count = 0
#define length of substring
sb_len = len(sb)
#loop to determing number of subtring in string
for i in range(len(s)):
    if s[i:i+sb_len] == sb:
        bob_count += 1

#print the number of times the substring appeared
print("Number of times bob occurs is: " + str(bob_count))
