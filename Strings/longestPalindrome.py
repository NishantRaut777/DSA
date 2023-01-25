# Got from disussions section little bit tricky

class Solution:
    def longestPalin(self, S):
        # code here
        if len(S) == 1:
            return S

        for i in range(len(S), 0, -1):
            for j in range(len(S)-i+1):
                x = S[j:i+j]
                if x == x[::-1]:
                    return x

s = Solution()
mystring = "aaaabbaa"
result = s.longestPalin(mystring)
print(result)