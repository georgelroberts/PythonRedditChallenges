"""
G. Roberts May 28th 2017

Problem 2 from http://www.shiftedup.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour
Write a function that combines two lists by alternatingly taking elements. For 
example: given the two lists [a, b, c] and [1, 2, 3], the function should 
return [a, 1, b, 2, c, 3]. 

My code also accounts for if the two lists are of unequal length.

"""

def mergeLists(list1, list2):
    mergedList=[]
    list1Size=len(list1)
    list2Size=len(list2)
    lengthToLoop=min(list1Size,list2Size)*2

    for i in range(lengthToLoop):
        if i%2==0:
            mergedList.append(list1[int(i/2)])
        else:
            mergedList.append(list2[int((i-1)/2)])

    if list1Size>list2Size:
        mergedList.extend(
            list1[int(lengthToLoop / 2) + i]
            for i in range(list1Size - list2Size)
        )
    elif list2Size>list1Size:
        mergedList.extend(
            list2[int(lengthToLoop / 2) + i]
            for i in range(list2Size - list1Size)
        )
    return mergedList
    
print(mergeLists(['a','b','c'],[1,2,3,4,5]))