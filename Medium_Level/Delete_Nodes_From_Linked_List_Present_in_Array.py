# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        remove_set = set(nums)  # convert list to set for O(1) lookups
        dummy = ListNode(0)     # dummy node before the head
        dummy.next = head
        current = dummy
        # Traverse the list and skip nodes whose value is in remove_set
        while current.next:
            if current.next.val in remove_set:
                current.next = current.next.next  # remove node
            else:
                current = current.next
        return dummy.next  # return new head
