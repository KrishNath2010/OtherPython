# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 09:40:14 2021

@author: Krish Nath
"""

trails=int(input())
answer_list=[]
for x in range(trails):
    lenth=int(input())
    numbers=input().split(' ')
    least=101
    count=0
    for s in numbers:
        use=int(s)
        #print(count)
        if use<least:
            count=1
            least=use
        elif use==least:
            count+=1
    answer_list.append(lenth-count)
for g in answer_list:
    print(g)
        