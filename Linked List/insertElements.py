# Question = Create a link list of size N according to the given input literals. Each integer input is accompanied by an indicator which can either be 0 or 1. If it is 0, insert the integer in the beginning of the link list. If it is 1, insert the integer at the end of the link list.


'''    
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''


class Solution:
    # Function to insert a node at the beginning of the linked list.
    def insertAtBegining(self, head, x):
        # code here
        begNode = Node(x)
        begNode.next = head
        return begNode

    # Function to insert a node at the end of the linked list.
    def insertAtEnd(self, head, x):
        # code here
        lastNode = Node(x)
        if head is None:
            return lastNode

        temp = head
        while temp.next is not None:
            temp = temp.next
        temp.next = lastNode
        return head
