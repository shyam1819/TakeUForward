class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge Case: If list is empty or has only one node, return as is
        if not head or not head.next:
            return head
        
        # Initialize pointers
        odd = head           # Starts at 1st node
        even = head.next     # Starts at 2nd node
        even_head = even     # Save the start of the even list to connect later
        
        # Traverse the list
        # We check even and even.next to ensure we can jump two nodes ahead
        while even and even.next:
            # Connect current odd node to the next odd node
            odd.next = even.next
            odd = odd.next
            
            # Connect current even node to the next even node
            even.next = odd.next
            even = even.next
            
        # Connect the end of the odd list to the head of the even list
        odd.next = even_head
        
        return head
