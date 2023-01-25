# Question => Given a string S consisting of lowercase Latin Letters. Return the first non-repeating character in S. If there is no non-repeating character, return '$'.

# Passing 1 test case


class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonrepeatingCharacter(self,s):
        #code here
        for i in range(len(s)):
            chartocheck = s[i]
            substr = s[i+1:]
            
            if chartocheck not in substr:
                return chartocheck
            elif chartocheck in substr:
                s = s.replace(chartocheck , "")

s = Solution()
mystr = "hqghumeaylnlfdxfircvscxggbwkfnqduxwfnfozvs"
result  = s.nonrepeatingCharacter(mystr)
print(result)