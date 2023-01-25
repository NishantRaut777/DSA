'''

#Linked list class
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        '''


class Solution:

    # Function to count nodes of a linked list.
    def getCount(self, head_node):
        # code here
        count = 1
        while head_node.next is not None:
            count += 1
            head_node = head_node.next
        return count
