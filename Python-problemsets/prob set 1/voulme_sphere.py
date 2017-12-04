'''
Name:Volume of sphere
Description: The volume of a sphere with radius r is 4/3pr3
Author:Rishi Kumar
Date:2/12/2017
'''
def volume_sphere(r):
    vol=float((4/3)*(22/7)*r*r*r)
    print "volume of sphere is " +str(vol)
r=int(raw_input("enter the radius: "))
volume_sphere(r)
