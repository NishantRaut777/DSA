class Solution:

    # Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self, a, b):
        # code here
        mydict_a = {}
        mydict_b = {}
        for i in a:
            if i in mydict_a.keys():
                mydict_a[i] = mydict_a[i] + 1
            else:
                mydict_a[i] = 1

        for i in b:
            if i in mydict_b.keys():
                mydict_b[i] = mydict_b[i] + 1
            else:
                mydict_b[i] = 1

        mydict_a = {key: val for key, val in sorted(
            mydict_a.items(), key=lambda ele: ele[0])}
        mydict_b = {key: val for key, val in sorted(
            mydict_b.items(), key=lambda ele: ele[0])}

        if mydict_a == mydict_b:
            return "YES"
        else:
            return "NO"


s = Solution()
a = "geeksforgeeks"
b = "forgeeksgeeks"
result = s.isAnagram(a,b)
print(result)


# steps:
# 1. create 2 empty dictionaries and for both strings create count of characters.
# 2. Sort the dictionaries by keys and compare. 
