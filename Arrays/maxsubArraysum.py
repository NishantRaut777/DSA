# question => Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.

class Solution:
    # Complete this function
    # Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self, arr, N):
        # Your code here
        sum = 0
        maxi = arr[0]

        for i in range(N):
            sum = sum + arr[i]

            maxi = max(sum, maxi)

            if sum < 0:
                sum = 0

        return maxi

s = Solution()
myarray = [1,2,3,-2,5]
N = len(myarray)
result = s.maxSubArraySum(myarray , N)
print(result)


# Steps:
# Use Kadane's Algorithm