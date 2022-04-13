# You are given two linked-lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwonumbers(self,l1,l2,c=0):






l1=ListNode(2)
l1.next=ListNode(4)
l1.next.next=ListNode(3)

l2=ListNode(5)
l2.next = ListNode(6)
l2.next.next=ListNode(4)

result= Solution.addTwonumbers(l1,l2)
while result:
    print result.val,
    result.next


