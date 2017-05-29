"""
G. Roberts May 28th 2017

Problem 1 from http://www.shiftedup.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour
Write three functions that compute the sum of the numbers in a given list using
 a for-loop, a while-loop, and recursion.

"""

def sumListFor(testList):
    total=0
    for i in testList:
        total+=i
    return total

def sumListWhile(testList):
    total=0
    i=0
    while i<len(testList):
        total+=testList[i]
        i+=1
    return total

def sumListRecurse(testList):
    if len(testList)==0:
        #print(testList)
        return 0
    else:
        return testList[0]+sumListRecurse(testList[1:])

print(sumListFor([3, 4, 1, 6, 26]))
print(sumListWhile([3, 4, 1, 6, 26]))
print(sumListRecurse([3, 4, 1, 6, 26]))