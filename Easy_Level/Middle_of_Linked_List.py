class Solution(object):
    def middleNode(self, head):
        slow=fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        return slow 
