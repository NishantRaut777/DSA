# Question = Given an array of digits (values are from 0 to 9), find the minimum possible sum of two numbers formed from digits of the array. All digits of the given array must be used to form the two numbers.

# Any combination of digits may be used to form the two numbers to be summed.  Leading zeroes are permitted.

# If forming two numbers is impossible (i.e. when n==0) then the "sum" is the value of the only number that can be formed.

class Solution:
    def minSum(self, arr, n):
        # Your code goes here
        if n == 1:
            return arr[0]
        arr.sort()
        n1,n2= '',''
        for i in range(0,n):
            if i%2==0:
                n1+=str(arr[i])
            else:
                n2+=str(arr[i])
        # print(n1,n2)
        return int(n1)+int(n2)



# steps:
# 1. Take 2 empty strings
# 2. sort the array.
# 3. create string of even indexed elements and odd indexed elements.
# 4. return sum of both strings.