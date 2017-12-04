'''
Name:Cover price of a book
Description:Suppose the cover price of a book is Rs.24.95, but bookstores get a 40% discount. Shipping costs
Rs.3 for the first copy and 0.75p for each additional copy. The total wholesale cost for
60 copies 
Author:Rishi Kumar
Date:2/12/2017
'''
def cover_price():
    a=0
    cp=float(raw_input("enter the cover price:"))
    d=float(raw_input("enter the discount %:"))
    sc1=float(raw_input("first copy shipping cost:"))
    sc2=float(raw_input("additional copies shipping cost"))
    n=int(raw_input("enter the no. of copies"))
    if(n==1):
      a=a+cp*(d/100)*sc1
    else:
      a=a+(cp*(d/100)*sc2*n)
    print "the wholesale cost is " + str(a)
  
cover_price()

