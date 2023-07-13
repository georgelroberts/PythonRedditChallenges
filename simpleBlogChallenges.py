"""
G. Roberts May 28th 2017

Problem 1 from http://www.shiftedup.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour
Write three functions that compute the sum of the numbers in a given list using
 a for-loop, a while-loop, and recursion.

"""

def sumListFor(testList):
    return sum(testList)

def sumListWhile(testList):
    return sum(testList[i] for i in range(len(testList)))

def sumListRecurse(testList):
    return 0 if len(testList)==0 else testList[0]+sumListRecurse(testList[1:])

print(sumListFor([3, 4, 1, 6, 26]))
print(sumListWhile([3, 4, 1, 6, 26]))
print(sumListRecurse([3, 4, 1, 6, 26]))