# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        
        rst = None
        for _ in range(len(lst)):
            rst = ListNode(lst[0], rst)
            del lst[0]
        
        return rst