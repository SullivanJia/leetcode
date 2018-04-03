# 给定两个非空链表来代表两个非负数，
# 位数按照逆序方式存储，它们的每个节点只存储单个数字。
# 将这两数相加会返回一个新的链表。
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(ListNode):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3=ListNode(l1.val+l2.val)
        while l1.next is not None and l2.next is None:
            l1 = l1.next
            l2 = l2.next
            l3.next=ListNode(l1.val+l2.val)
            l3=l3.next
        return l3





