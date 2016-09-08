#1.
#print("Twinkle, twinkle, little star,\n\tHow I wonder what you are! \n\t\tUp above the world so high,\n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are")
#2.
#import sys
#print (sys.version)
#3.
#import datetime
#now = datetime.datetime.now()
#print("Current date and time: ")
#print(now.strftime("%m-%d-%Y %H:%M:%S"))
#4.
#from math import pi  
#r = float(input ("Input the radius of the circle: "))  
#print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2)) 
#5.
#firstname = input("What is your first name: ")
#lastname = input("What is your last name: ")
#print ("Hello " + lastname + " " + firstname)
#6.
#values = input("Enter comma separated numbers: ")
#list = values.split(",")
#tuple = tuple(list)
#print("List: ",list)
#print("Tuple: ",tuple)
#7.
#filename = input("Enter file name: ")
#extension = filename.split(".")
#print ("Your file type is: " + repr(extension[-1]))
#8.
#color_list = ["Red","Green","White" ,"Black"]
#print("%s %s" % (color_list[0], color_list[3]))
#9.
#exam_st_date = (11, 12, 2014)
#print ("The exam starts: %i/%i/%i" %exam_st_date)  
#10.
#a = int(input("Input an integer : "))  
#n1 = int( "%s" % a )  
#n2 = int( "%s%s" % (a,a) )  
#n3 = int( "%s%s%s" % (a,a,a) )  
#print (n1+n2+n3) 
#11.
#print(abs.__doc__) 
#12.
#import calendar
#y=int(input("Year: "))
#m=int(input("Month: "))
#print(calendar.month(y,m))
#13.
#print(""" 
#a string that you "don't" have to escape 
#This 
#is a  ....... multi-line 
#heredoc string --------> example 
#""")  
#14.
#from datetime import date
#f_date = date(2014, 7, 2)  
#l_date = date(2014, 7, 11)  
#difference = l_date - f_date  
#print(difference.days)  
#15.
#pi = 3.1415926535897931  
#r= 6.0  
#V= 4.0/3.0*pi* r**3  
#print('The volume of the sphere is: ',V)  
#16.
#def difference(n):  
#    if n <= 17:  
#        return 17 - n  
#    else:  
#        return (n - 17) * 2   
#print(difference(22))  
#print(difference(14))  
#17.
def near_thousand(n):  
      return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))  
print(near_thousand(1000))  
print(near_thousand(900))  
print(near_thousand(800))     
print(near_thousand(2200))  
18.
def sum_thrice(x, y, z):  
  
     sum = x + y + z  
    
     if x == y == z:  
      sum = sum * 3  
     return sum  
  
print(sum_thrice(1, 2, 3))  
print(sum_thrice(3, 3, 3))  
19.
