
# Passing only 5 test cases
def findTriplets(self, arr, n):
    # code here
    arr.sort()
    for i in range(n):
        low = i+1
        high = n-1

        target = 0 - arr[i]

        while low < high:
            if (arr[low] + arr[high]) == target:
                return 1
            elif (arr[low] + arr[high]) > target:
                high = high - 1
            elif (arr[low] + arr[high]) < target:
                low = low + 1
        return 0



# Steps:
# 1. use pointers low to point next element to ith element and high to last element.
# 2. Use target variable with mathematical value " 0 - arr[i]" because we will compare this value.
# 3. We used above formula because "arr[low] + arr[high] + arr[i] = 0" is our requirement.