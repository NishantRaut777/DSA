# I Tried :
def printsecondlargest(arr):
    maxnum = -1
    for i in arr:
        if i > maxnum:
            maxnum = i
        elif i == maxnum:
            arr.remove(i)
    arr.remove(maxnum)
    arr.sort()
    secondlargest = arr[-1]
    return secondlargest


myarr = [12, 35, 1, 10, 34, 1]
answer = printsecondlargest(myarr)
print(answer)


# correct Answer: all test case passed
def print2largest(self, arr, n):
    
    largest = -(math.inf)
    for i in arr:
        if i > largest:
            largest = i

    second_largest = -(math.inf)

    for i in arr:
        if i > second_largest and i != largest:
            second_largest = i

    if second_largest == -(math.inf):
        return -1
    else:
        return second_largest




# Steps:
# 1. Assign lowest value to "largest" variable and loop in array to find maximum value.
# 2. Assign lowest value to "second_largest" variable and check if "i > second_largest and i != largest" and find second largest.
