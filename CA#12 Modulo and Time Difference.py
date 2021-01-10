# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 14:04:19 2020

@author: 
    
    
Dealing with remainders may cause heavy headache to novice programmers. 
Let us write a simple program which has this operation for its core to study 
integer division better. At the same time we'll have some practice in handing dates - 
which sometimes gives headache even to experienced coders.

In arithmetic, the remainder (or modulus) is the amount "left over" after performing 
the division of two integers which do not divide evenly (from Wiki). This task will 
provide further practice with modulo operation.

Suppose, we are given two timestamps - for example, when the train or ferry boat 
starts its travel and when it finishes. This may look like:

start: May 3, 17:08:30
end  : May 8, 12:54:15
and we are curious to know, how much time (in days, hours, minutes and seconds) is 
spent in traveling (perhaps, to choose faster variant). How this could be achieved?

One of the easiest way is:

convert both timestamps to big numbers, representing seconds from the beginning of 
the month (or year, or century);
calculate their difference - i.e. travel time in seconds;
convert this difference back to days, hours, minutes and seconds.
First operation could be performed by multiplying minutes by 60 and hours by 60*60 etc. 
and summing all values up.
The third operation should be performed on contrary by several divisions with keeping remainders.

In this task we are given several pair of timestamps. We suppose that both dates in the
 pair are always in the same month, so only number of day will be given. We want to calculate 
 difference between timestamps in each pair.

Input data: the first line contains number of test-cases, other lines contain test-cases themselves.
Each test-case contains 8 numbers, 4 for each timestamp: day1 hour1 min1 sec1 day2 hour2 min2 sec2 
(second timestamp will always be later than first).
Answer: for each test-case you are to output difference as following (days hours minutes seconds) - 
please note brackets - separated by spaces.

Example:

input data:
3
1 0 0 0 2 3 4 5
5 3 23 22 24 4 20 45
8 4 6 47 9 11 51 13

answer:
(1 3 4 5) (19 0 57 23) (1 7 44 26)
"""
second = 1
minute = second *60
hour = second *60*60
day = hour * 24
total1 = 0
total2 = 0
d3, h3, m3, s3 = 0, 0, 0, 0

alist = input().split()
zlist = zip(alist[0::8],alist[1::8],alist[2::8],alist[3::8],alist[4::8],alist[5::8],alist[6::8],alist[7::8],)
#print(list(zlist))
for d1,h1,m1,s1,d2,h2,m2,s2 in zlist:
    #print(d1)
    total1 = (int(d1) * day)+(int(h1)*hour)+(int(m1)*minute) + int(s1)
    total2 = (int(d2) * day)+(int(h2)*hour)+(int(m2)*minute) + int(s2)
    total3 = total2 - total1
    d3 = total3/day
    total3 = total3%day
    
    h3 = total3/hour
    total3 = total3%hour
    
    m3 = total3/minute
    total3 = total3%minute
    
    s3 = total3
    
    print("(" + str(int(d3)) + " " + str(int(h3)) + " " + str(int(m3)) + " " + str(int(s3)) + ")")

