'''
Name:Eval_loop
Description: A function called eval_loop that iteratively prompts the user, takes the resulting input and evaluates it using eval, and prints the result. It continues until the user enters 'done', and then return the value of the last expression it evaluated.
Author:Rishi Kumar
Date:2/12/2017
'''
import math
def eval_loop(n):
    e=eval('%s' % n)
    print e
    a=raw_input("Enter another expression or done if finished")
    if(a=='done'):
        print "The last result is ",e
    else:
        eval_loop(a)


n=raw_input("Enter the expression:")
eval_loop(n)