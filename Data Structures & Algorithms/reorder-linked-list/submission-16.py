# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        

        # find head of the second half (h2)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        
        # reverse 2nd half of list
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next
        

        # rearrage list
        curr_1 = head
        curr_2 = prev

        while curr_2:
            next1 = curr_1.next
            next2 = curr_2.next
            curr_1.next = curr_2
            curr_2.next = next1
            curr_1 = next1
            curr_2 = next2
        

        