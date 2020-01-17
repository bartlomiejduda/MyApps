import sys
import datetime
from math import pi

# Exercises - https://www.w3resource.com/python-exercises/python-basic-exercises.php
#print(sys.version)
#now = datetime.datetime.now()
#print("Cur date: " + now.strftime("%Y-%m-%d %H:%M:%S"))
#r = float(input("Input r: "))
#print("pi*r^2 = " + str(pi * r**2))

#zad5
#name = input("Name: ")
#surname = input("Surname: ")
#print(surname + " " + name)

#zad6
#vals = input("Vals: ")
#list1 = vals.split(',')
#tuple1 = tuple(list1)
#print(list1)
#print(tuple1)

#zad7
#filename1 = input("Filename: ")
#ext1 = filename1.split('.')[-1]
#print('Ext: ' + str(ext1))

#zad8
#color_list = ["Red","Green","White" ,"Black"]
#print(color_list[0] + " " + color_list[-1])

#zad9
#exam_st_date = (11, 12, 2014)
#print("St date: %i/%i/%i"%exam_st_date)

#zad10
#n = int(input("n: "))
#w = n + (n*n) + (n*n*n) 
#print("w: " + str(w))

#zad11
#def my_fun():
    #'''Returns 1'''
    #return 1

#print(abs.__doc__)
#print(my_fun.__doc__)
#print(int.__doc__)

#zad12
#import calendar 
#mon = int(input("Month: "))
#year = int(input("Year: "))
#print(calendar.month(year, mon))

#zad13
#str1 = '''a string that you "don't" have to escape
#This
#is a ....... multi-line
#heredoc string --------> example'''
#print(str1)

#zad14
#Sample dates : (2014, 7, 2), (2014, 7, 11)
#Expected output : 9 days 

#date1 =  datetime.date(2014, 7, 2)
#date2 = datetime.date(2014, 7, 11)
#print(date2 - date1)

#zad15
#r = 6
#V = (4.0/3.0) * pi * r**3
#print("V: " + str(V))

#zad16
#num = int(input("num: "))
#w = abs(num - 17)
#if num > 17:
    #w = w*2
#print("Diff: " + str(w))

#zad17
#def near(num):
    #if ((abs(num-1000) <= 100) or (abs(num-2000) <= 100)):
        #return True
    #else:
        #return False
    
#print(near(1000))
#print(near(900))
#print(near(800))
#print(near(2200))

#zad18
#n1 = int(input("n1: "))
#n2 = int(input("n2: "))
#n3 = int(input("n3: "))
#s1 = n1 + n2 + n3 
#if n1 == n2 and n2 == n3:
    #s1 = s1 * 3
#print("s1: " + str(s1))

#zad19
#def ret_str(str1):
    #if len(str1)>2 and str1[:2] == "Is":
        #return str1
    #else:
        #return "Is" + str1 
    
#print(ret_str("Array"))
#print(ret_str("IsEmpty"))

#zad20
n1 = int(input("n1: "))
str1 = str(input("str1: "))

    