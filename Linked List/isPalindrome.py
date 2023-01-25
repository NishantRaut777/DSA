class Solution:
    def isPalindrome(self, head):
        #code here
        mystr = ""
        while head != None:
            mystr += str(head.data)
            head = head.next
            
        
            
        myrevstr = mystr[-1::-1]
        
        if mystr == myrevstr:
            return 1
        else:
            return 0


# Steps:
# 1. Create string and then find reverse of string and then compare