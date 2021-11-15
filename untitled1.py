# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 10:22:21 2021

@author: Krish Nath
"""
trails=1
answer_list=[]
for x in range(trails):
    number=int(input())
    digts=len(str(number))
    #print(digts)
    def caculate(number,digts):
        base=1
        prev=0
        for d in range(digts):
            prev+=base
            base*=10
        if number%prev==0:
            answer=digts*number//prev
            return answer
        close=abs(number-prev)
        closest=prev
        for a in range(10):
            use=a+2
            va=abs((use*prev)-number)
            if va<close:
                close=va
                closest=use
        answer=0
        if closest<7:
            answer+=digts*closest+caculate(close,len(str(close)))
        else:
            answer+=digts*(12-closest)+1
        return answer
    fin_answer=caculate(number,digts)
    answer_list.append(fin_answer)
for g in answer_list:
    print(g)