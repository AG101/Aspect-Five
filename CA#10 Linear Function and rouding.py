# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 12:54:50 2020

@author: Aspect

Very common problem in computational programming is to determine the underlying 
law to which some phenomenon obeys. For learning purpose let us practice a simple 
variant - discovering linear dependence by two given observations (for example, 
how the price for some product depends on its size, weight etc.)

Linear function is defined by an equation:

y(x) = ax + b
Where a and b are some constants.
For example, with a=3, b=2 function will yield values y = 2, 5, 8, 11...
for x = 0, 1, 2, 3...

Your task is to determine a and b by two points, belonging to the function.
I.e. you are told two pairs of values (x1, y1), (x2, y2) which satisfy the function 
equation - and you should restore the equation itself.

Input data have the number of test-cases in the first line
and then test-cases themselves in separate lines.
Each case contains 4 integers (x1 y1 x2 y2).
Answers should be integer too and you are to write them in line, separating with 
spaces and enclosing each pair in parenthesis, for example:

input data:
2
0 0 1 1
1 0 0 1

answer:
(1 0) (-1 1)
"""
def rounding(i):
    #in theory it takes i and all this does is churn it out
    
    if i > 0:
        if i - int(i) >= 0.5:
            i = int(i) + 1
        else:
            i = int(i)
    elif i < 0:
        if abs(i) - abs(int(i)) >= 0.5:
            i = int(i) - 1
        else:
            i = int(i)
    return(i)

alist = input().split()
#zip it into 4 i guess
zlist = zip(alist[0::4],alist[1::4],alist[2::4],alist[3::4])
#print(list(zlist))
a = 0
b = 0
t=[]

for x1,y1,x2,y2 in zlist:
    a = rounding((int(y2) - int(y1))/(int(x2) - int(x1)))
    #rounding(a)
    #print(a)
    b = rounding(int(y1) - (int(a)*int(x1)))
    #rounding(b)
    #print(b)
    t = "(" + str(a) + " " + str(b) +")"
    print(t)
    
