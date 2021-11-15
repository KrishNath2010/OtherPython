# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 16:08:30 2020

@author: Krish Nath
"""
import random , pylab
# helper function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std  
  
def guessfood_sim(num_trials, probs, cost, get):
    """
    num_trials: integer, number of trials to run
    probs: list of probabilities of guessing correctly for 
           the ith food, in each trial
    cost: float, how much to pay for each food guess
    get: float, how much you get for a correct guess
    
    Runs a Monte Carlo simulation, 'num_trials' times. In each trial 
    you guess what each food is, the ith food has 'prob[i]' probability 
    to get it right. For every food you guess, you pay 'cost' dollars.
    If you guess correctly, you get 'get' dollars. 
    
    Returns: a tuple of the mean and standard deviation over 
    'num_trials' trials of the net money earned 
    when making len(probs) guesses
    """
    list_for_meanStd=[]
    for x in range(num_trials):
        money=0.0
        for index in range(len(probs)):
            prob=probs[index]
            money-=cost
            random_num=random.random()
            if random_num<=prob:
                money+=get
        list_for_meanStd.append(money)
    answer=getMeanAndStd(list_for_meanStd)
    return answer 

# print(guessfood_sim(3000, [0.5, 0.5, 0.5], 1, 1))



# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title!=None:
        pylab.title(title)
    pylab.show()
        
    
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    trils_rsult=[]
    sum=0
    for roll_num in range(numTrials):
        roll=[]
        for trail in range(numRolls):
            roll.append(die.roll())
        gratest=0
        current=0
        previous=roll[0]
        for x in range(len(roll)):
            current_number=roll[x]
            if current_number==previous:
                current+=1
                if current>gratest:
                    gratest=current
            else :
                current=0            
            previous=roll[x]
        trils_rsult.append(gratest)
    for x in trils_rsult:
        sum+=x
    average=sum/len(trils_rsult)
    makeHistogram(trils_rsult, 10, 'longest run of a number', 'number of times it oucrues')
    return round(average,3)
        
            
    
# One test case
#print(getAverage(Die([1,2,3,4,5,6]), 50, 1000))
import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
import numpy as np
def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over. 
    """
    numpy_choices=np.array(choices)
    greatest=0
    num_ones_for_greatest = 0
    graet_answer=np.array([],dtype=np.int32)
    for i in range(len(choices)):
        graet_answer=np.append(graet_answer, 0)
    #graet_answer=np.zeros(len(choices))
    least=10000
    lenth_chocies=len(choices)
    for d in range((lenth_chocies**3)*4):
        a=np.array([],dtype=np.int32)
        sum_total=0
        num_ones=0
        for x in range(lenth_chocies):
            random_chocic=random.choice([0,1])
            num_ones += random_chocic
            a=np.append(a, random_chocic)
            sum_total+=random_chocic*numpy_choices[x]
        if sum_total>=greatest and sum_total<=total:
            if (sum_total==greatest):
                if (num_ones_for_greatest > num_ones):
                    graet_answer=a
                    num_ones_for_greatest = num_ones
                    #print("replaced", a)
                    #print("total", sum_total)
            else:
                graet_answer=a
                num_ones_for_greatest = num_ones
                #print("set", a)
                #print("total", sum_total)
            greatest=sum_total
    return graet_answer
print(find_combination([3, 10, 2, 1, 5], 12))        