# Question = Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S and return the left and right index(1-based indexing) of that subarray.


def subArraySum(arr, n, s):
    if n == 1 and arr == s:
        return 1
    else:
        start = 0
        while start < n:
            end = start
            sum = 0
            while end < n:
                sum = sum+arr[end]
                if sum < s:
                    end += 1
                elif sum > s:
                    break
                else:
                    return [start+1, end+1]
            start += 1
    return [-1]

myarray = [1, 2, 3, 7, 5]
n = len(myarray)
s = 12
result = subArraySum(myarray, n, s)
print(result)



# Steps:
# 1. Create start pointer which will be fixed for current iteration and end pointer will be moving pointer.
# 2. keep sum as 0 at start of each iteration and keep adding sum to moving pointer till "end < n"
# 3. If at any point it becomes equal then return output.