# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1) Dummy node to simplify edge-cases (like removing the first real node)
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        # 2) Advance `fast` n+1 steps ahead, so the gap between fast/slow is n nodes
        for _ in range(n + 1):
            fast = fast.next

        # 3) Move both pointers until fast hits the end
        #    At that point, slow is right before the node to delete
        while fast:
            fast = fast.next
            slow = slow.next

        # 4) Skip over the target node
        #    slow.next is the nth node from the end
        slow.next = slow.next.next

        # 5) Return the new head (might have changed if we removed the original first node)
        return dummy.next
