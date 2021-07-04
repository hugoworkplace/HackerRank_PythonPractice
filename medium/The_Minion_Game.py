#!/usr/bin/env python3
"""
Game Rules

Both players are given the same string S, .
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string S.

For Example:
String  S = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

For better understanding, see the image below:
https://www.hackerrank.com/challenges/the-minion-game/problem

Function Description

Complete the minion_game in the editor below.

minion_game has the following parameters:
	string string: the string to analyze
Prints
	string: the winner's name and score, separated by a space on one line, or Draw if there is no winner

Input Format

A single line of input containing the string S.
Note: The string  will contain only uppercase letters: [A-Z].

Constraints
0<len(S)<=10^6


Sample Input
BANANA

Sample Output
Stuart 12

Note :
Vowels are only defined as AEIOU. In this problem,  is not considered a vowel.
"""


#Solution -   starter of a substring, and add 

def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'

    kevsc = 0
    stusc = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kevsc += (len(string)-i)
        else:
            stusc += (len(string)-i)

    if kevsc > stusc:
        print("Kevin", kevsc)
    elif kevsc < stusc:
        print("Stuart", stusc)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)

"""
#Solution - nested loops cause Run time error 
def minion_game(string):
    Stuart = 0
    Kevin = 0
    vowels = ['A','E','I','O','U']
    li = []
    #length of substring
    for i in range(1, len(string)+1):
        
        #start from first char
        for j in range(len(string)):
            if j+i <= len(string):
                li.append(string[j:j+i])
 
    for item in li:
        if item[0] in vowels:
           Kevin+=1
        else:
           Stuart+=1
        
   
            
    #print(li)
    if Stuart > Kevin:
        print('Stuart '+str(Stuart))
    elif Stuart == Kevin:
        print('Draw')
        
    else:
        print('Kevin '+str(Kevin))

"""
