# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 15:05:56 2020

@author: Aspect

This problem provides an exercise for learning core idea of infamous ordering 
algorithm - bubble sort - which we are supposed to learn a bit later.

Given integer array, we are to iterate through all pairs of neighbor elements, 
starting from beginning - and swap members of each pair where first element is
 greater than second.

For example, let us consider small array of elements 1 4 3 2 6 5, marking which 
pairs are swapped and which are not:

(1  4) 3  2  6  5  - pass
1 (4  3) 2  6  5  - swap
1  3 (4  2) 6  5  - swap
1  3  2 (4  6) 5  - pass
1  3  2  4 (6  5) - swap
1  3  2  4  5  6  - end
This operation moves some greater elements right (to the end of array) and some 
smaller elements left (to the beginning).
What is the most important: the largest element is necessarily moved to the last 
position.

Input data contain sequence of elements of the array, all positive. After this 
value -1 follows to mark the end (it should not be included into an array).
Answer should contain two values - number of performed swaps and checksum of the
 array after processing (separated by spaces).
Checksum should be calculated with exactly the same method as in the task Array 
Checksum

Example:

input data:
1 4 3 2 6 5 -1

answer:
3 5242536
"""
def checksum(anylist):
    result = 0
    for i in anylist:
        result = ((result + int(i))*113)%10000007
    return(result)
alist =input().split()

counter = 0
swap = 0
for i,j in (zip(alist, alist[1::])):
    if int(i) >= int(j):
        alist[counter] = j
        alist[counter +1] = i
        swap+=1
    counter +=1
    print(swap, checksum(alist))
        