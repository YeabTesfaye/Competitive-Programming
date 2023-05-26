class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        node = head
        n = 0
        while node:
            node = node.next
            n += 1
        
        if n == 1:
            return None
        
        node = head
        for i in range(n // 2 - 1):
            node = node.next
        
        #skip the middle node 
        node.next = node.next.next
        
        return head
