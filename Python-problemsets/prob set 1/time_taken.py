'''
Name:time_taken
Description: If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
Author:Rishi Kumar
Date:2/12/2017
'''
t1=float(raw_input("enter the starting time"))
t2=t1*60
e=int(raw_input("enter easy pace(miles travelled:"))
t=int(raw_input("enter tempo pace(miles travelled):"))
tot=((e*(8/15))+(t*(7/12)))*60
time=float((tot+t1)/60)
print "time when you reach home "+str(time)
