'''
Name:Binary to Decimal
Description: To write a program that computes the decimal equivalent of the binary numbers
Author:Rishi Kumar
Date:2/12/2017
'''

binary = raw_input('enter a number: ')
decimal = 0
for digit in binary:
    decimal = decimal*2 + int(digit)
print decimal
