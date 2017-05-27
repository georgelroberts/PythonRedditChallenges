"""
G. Roberts May 25th 2017

Given a list of integers separated by a single space on standard input, print 
out the largest and smallest values that can be obtained by concatenating the 
integers together on their own line. This is from Five programming problems 
every Software Engineer should be able to solve in less than 1 hour, problem 4.
 Leading 0s are not allowed (e.g. 01234 is not a valid entry). 

My solution pads each number to be the same length for a size comparison. It
also accounts for the fact that this padding will give the wrong answer 
sometimes by adding a value if there is padding so it will always be the 
correct number upon comparison.
"""

def sortByNumbers(numString):
    listOfStrs = numString.split()
    noItems=len(listOfStrs)
    newList=[]
    maxLength=max(len(s) for s in listOfStrs)
    for i in listOfStrs:
        while len(i)<maxLength:
            if len(i)==maxLength-1 and len(i)==1:
                i+='0.99'
            elif len(i)==maxLength-1:
                i+='9.99'
            else:
                i+='0'
        newList.append(i)
        
    sortedByIndex=sorted(range(noItems), key=lambda k: newList[k])
    maxNumber=''
    minNumber=''
    for i in range(noItems):
        minNumber+=listOfStrs[sortedByIndex[i]]
        maxNumber+=listOfStrs[sortedByIndex[noItems-i-1]]
    return int(minNumber), int(maxNumber)


print(sortByNumbers('5 56 50'))
print(sortByNumbers('79 82 34 83 69'))
print(sortByNumbers('420 34 19 71 341'))
print(sortByNumbers('17 32 91 7 46'))