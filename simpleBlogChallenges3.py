"""
G. Roberts May 28th 2017

Write a function that computes the list of the first 100 Fibonacci numbers. By 
definition, the first two numbers in the Fibonacci sequence are 0 and 1, and 
each subsequent number is the sum of the previous two. As an example, here are 
the first 10 Fibonnaci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.
"""

def fibonacci():
    first=0
    second=1
    print(first)
    for i in range (99):
        print(second)
        temp=second
        second=second+first
        first=temp

fibonacci()