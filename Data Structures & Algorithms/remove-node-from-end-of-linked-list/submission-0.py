# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return None
        
        list_size = 0
        curr = head
        while curr:
            list_size += 1
            curr = curr.next
        
        rem = list_size - n
        prev = None
        curr = head
        for i in range(rem):
            prev = curr
            curr = curr.next
        
        if prev == None:
            head = curr.next
        else:
            prev.next = curr.next
        
        curr.next = None

        return head
        

        

        