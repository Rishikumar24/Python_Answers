'''
Name:Palindrome_check
Description:To build a test function palindrome_check() that tests your palindrome function
Author:Rishi Kumar
Date:2/12/2017
'''
def palindrome_check(s1):  
    s2=reversed(s1)
    if(list(s1)==list(s2)):
        print "It is a palindrome"
    else:
        print "It is not a palindrome"

s1=raw_input("Enter a string")
palindrome_check(s1)