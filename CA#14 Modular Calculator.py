# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 14:31:33 2020

@author: Aspect

This task provides practice for core property of remainder taking operation in 
arithmetic - persisting of the remainder over addition and multiplication. This 
important property is often used for checking results of calculations, in competitive 
programming, in calculation checksums and especially for encryption.
See Modular arithmetic for thorough explanations.

We have a kind of long arithmetic calculation here, and we are asked about the result
 modulo some number (result % M in many languages).

If you are curious why modular arithmetic is that important, you can see Public Key 
Cryptography Intro and RSA Cryptography exercises.

Input data will have:

initial integer number in the first line;
one or more lines describing operations, in form sign value where sign is either + or * 
and value is an integer;
last line in the same form, but with sign % instead and number by which the result 
should be divided to get the remainder.
Answer should give remainder of the result of all operations applied sequentially 
(starting with initial number) divided by the last number.

If you have troubles with this problem, please feel free to type its name in the 
"Search" box in the top menu and find relevant topics at our forum - probably you will 
get enough enlightenment from there.

Example:

input data:
5
+ 3
* 7
+ 10
* 2
* 3
+ 1
% 11

answer:
1
In this case result after all operations applied sequentially is 397.
"""
alist = input().split()
#print(alist)
total = 0
zlist = zip(alist[1::2], alist[2::2])
total = alist[0]
for sign,num in zlist:
    if sign == '+':
        total = int(total) + int(num)
        #print(f"running total + {num} = {total}")
    elif sign == "*":
        total = int(total) * int(num)
        #print(f"running total * {num} = {total}")
    elif sign == "%":
        total = int(total)%int(num)
        #print(f"running total mod {num} = {total}")
        print(total)

