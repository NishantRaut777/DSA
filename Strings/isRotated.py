class Solution:
    #Function to check if a string can be obtained by rotating
    #another string by exactly 2 places.
    def isRotated(self,str1,str2):
        #code here
        temp1 = str1[0:2]
        temp2 = str1[2: ]
        anticlockwisestr = temp2 + temp1
        
        temp3 = str1[0:len(str1) - 2]
        temp4 = str1[len(str1) - 2: ]
        clockwisestr = temp4 + temp3
        
        if str2 == anticlockwisestr:
            return 1
        elif str2 == clockwisestr:
            return 1
        else:
            return 0

s = Solution()
str1 = "amazon"
str2 = "azonam"
result = s.isRotated(str1 , str2)
print(result)


# steps:
# 1. Find anticlockwise and clockwise direction values and compare.