# 合并两个已排序的链表，并将其作为一个新列表返回。新列表应该通过拼接前两个列表的节点来完成。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        pass



if __name__ == '__main__':
    l1=0
    for i in range(5):
        l1=ListNode(i)
        l1.next=l1
        print(l1.val)
    # print(l1.next.val)




