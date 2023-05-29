# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        ### Brute Force 
        
        current  = head
        nodes = []
        while current!= None:
            nodes.append(current.val)
            current  = current.next 
        l,r = 0,len(nodes) - 1
        output = []
        while l < r:
            output.append(nodes[l] + nodes[r])
            l += 1
            r -= 1

        return max(output)
        