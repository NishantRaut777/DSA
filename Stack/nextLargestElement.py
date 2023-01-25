class Solution:
    def nextLargerElement(self, arr, n):
        # code here
        res = []
        stack = []
        i = 0
        while i < n:
            res.append(-1)

            if len(stack) == 0 or arr[i] < stack[-1][0]:
                stack.append([arr[i], i])
            else:
                while len(stack) > 0 and arr[i] > stack[-1][0]:
                    res[stack[-1][1]] = arr[i]
                    stack.pop()
                stack.append([arr[i], i])
            i += 1
        return res

s = Solution()
arr = [1 ,3 ,2 ,4]
n = 4
result = s.nextLargerElement(arr,n)
print(result)


# steps:
# 1. We have 2 lists. "res" and "stack".
# 2. In stack we are storing current value along with index.
# 3. First we are checking if length of stack is equal to zero or current element is less than last element in stack if YES then we directly append that value along with index in stack.
# 4. Else while stack length is greater than zero and current element is greater than stack element we change the value in "res" list ( THis step is tricky )and we pop that element from stack
# 5. And we make sure that we append current element in stack after completing while loop. 