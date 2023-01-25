# Not passing all test cases and not used heap concept in this

# Given an array of N positive integers, print k largest elements from the array. 

class Solution:
    # Function to return k largest elements from an array.
    def kLargest(self, li, n, k):
        # code here
        finalelements = []

        while k > 0:
            maxele = 0
            for i in li:
                if i > maxele:
                    maxele = i
            finalelements.append(maxele)
            li.remove(maxele)
            k = k - 1

        return finalelements

s = Solution()
li = [12,5,787,1,23]
n = len(li)
k = 2
result = s.kLargest(li , n , k)
print(result)
