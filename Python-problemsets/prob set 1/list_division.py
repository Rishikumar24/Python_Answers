'''
Name:List division
Description: def getRatios(vect1, vect2):
	"""Assumes: vect1 and vect2 are lists of equal length of numbers
	Returns: a list containing the meaningful values of
	vect1[i]/vect2[i]"""
Author:Rishi Kumar
Date:2/12/2017
'''
vect1 = [10, 30, 100, 80, 125]
vect2 = [5, 10, 20, 20, 25]
a = []

end = len(vect1)
def getRatios(vect1,vect2):
  for i in range(end):
    a.append(float(vect1[i]/vect2[i]))
getRatios(vect1,vect2)
print a
