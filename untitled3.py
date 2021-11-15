# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 09:33:21 2021

@author: Krish Nath
"""
def find_power(lower,upper):
   result=1
   use_1=lower*2
   while True:
      if use_1*2<upper:
          use_1=use_1*2
          result+=1
      else:
          break
   return result
trails=int(input())
answer_list=[]
for x in range(trails):
    number=int(input())
    numbers=input().split(' ')
    index=-1
    answer=0
    for s in numbers:
        index+=1
        if index==number-1:
            break
        use=int(s)
        next_use=int(numbers[index+1])
        if next_use>2*use:
            answer+=find_power(use,next_use)
        elif next_use*2<use:
            answer+=find_power(next_use,use)
    answer_list.append(answer)
for g in answer_list:
    print(g)