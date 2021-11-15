# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 09:33:35 2021

@author: Krish Nath
"""
trails=int(input())
answer_list=[]
for x in range(trails):
    number=int(input())
    numbers=input().split(' ')
    avg=int(number/3)
    c_0=0
    c_1=0
    c_2=0
    for s in numbers:
        use=int(s)
        mod=use%3
        if mod==0:
            c_0+=1
        elif mod==1:
            c_1+=1
        else:
            c_2+=1
    #print(c_0,c_1,c_2)
    if c_0==c_1 and c_0==c_2:
        answer_list.append(0)
    else: 
        if c_0>=c_1 and c_0>=c_2:
            biggest=c_0
        if c_1<=c_0 and c_1>=c_2:
            biggest=c_1
        if c_2>=c_0 and c_2>=c_1:
            biggest=c_2
        if c_0==avg or c_1==avg or c_2==avg :
            if c_0>c_1 or c_1>c_2 or c_2>c_0:
                answer_list.append(biggest-avg)
            else:
                answer_list.append(2*(biggest-avg))
        else:
            if c_0<=c_1 and c_0<=c_2:
                smallest=c_0
            if c_0>=c_1 and c_1<=c_2:
                smallest=c_1
            if c_1>=c_2 and c_0>=c_2:
                smallest=c_2
            answer_list.append(biggest-smallest)
for g in answer_list:
    print(g)
