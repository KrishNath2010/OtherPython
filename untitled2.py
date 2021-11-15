# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 12:20:15 2021

@author: Krish Nath
"""

trails=int(input())
answer_list=[]
for x in range(trails):
    numbers=input().split(' ')
    n=int(numbers[0])
    k=int(numbers[1])
    if n%2==0:
        answer=int(((n-1)%k)+1)
        answer_list.append(answer)
    else:
         if k==1:
             answer_list.append(1)
         else:
            new_k=k+k/(n//2)
            answer=int((new_k%(n-1))+1)
            answer_list.append(answer)
for g in answer_list:
    print(g)