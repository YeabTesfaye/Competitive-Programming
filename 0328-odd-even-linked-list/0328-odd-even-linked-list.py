# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None or head.next.next is None:
            return head
        current = head
        dummy = head.next 
        odd = head
        even = head.next

        while odd and odd.next and even and even.next:
            odd.next = odd = odd.next.next
            even.next = even = even.next.next
        odd.next = dummy 
        return head
        