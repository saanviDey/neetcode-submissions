# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return None
        
        first = head
        for i in range(n):
            first = first.next

        second = ListNode(0, head)

        while first:
            second = second.next
            first = first.next
        
        if second.next == head:
            head = second.next.next
        second.next = second.next.next
        return head

        

        

        