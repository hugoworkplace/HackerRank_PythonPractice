#!/usr/bin/env python3
"""

In the Gregorian calendar, three conditions are used to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.

Task

Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

Input Format

Read year, the year to test.

Constraints

1900 <= year <= 10^5

Output Format

The function must return a Boolean value (True/False). Output is handled by the provided code stub.


Sample Input
1990

Sample Output
False

Explanation
1990 is not a multiple of 4 hence it's not a leap year.

"""



def is_leap(year):
    leap = False
        
    # Write your logic here
    if year % 400 == 0:
        leap = True
    elif year % 4 == 0 and year % 100 != 0:
        leap = True
        
    
    return leap

year = int(input())
print(is_leap(year))
