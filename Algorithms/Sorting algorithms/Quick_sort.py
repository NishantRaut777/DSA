import random

def findPivot(mylist,first,last):
    # To set pivot at random index
    # rindex = random.randint(first,last)
    # mylist[first] , mylist[rindex] = mylist[rindex] , mylist[first]


    # setting pivot as first element
    pivot = mylist[first]
    left = first + 1
    right = last

    while True:
        while left <= right and mylist[left] <= pivot:
            left = left + 1
    
        while left <= right and mylist[right] >= pivot:
            right = right - 1

        if right < left:
            break
        else:
            mylist[left] , mylist[right] = mylist[right] , mylist[left]
    
    mylist[first] , mylist[right] = mylist[right] , mylist[first]
    # when we set pivot as first we return right and when we set pivot as last then we return left
    return right


def quicksort(mylist,first,last):
    if first < last:
        p = findPivot(mylist,first,last)
        quicksort(mylist,first,p-1)
        quicksort(mylist,p+1,last)
        
    


mynewlist = [56,26,93,17,31,44]
n = len(mynewlist)
quicksort(mynewlist,0,n-1)
print(mynewlist)



    



