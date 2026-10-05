# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # Insertion in heap (min)
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode()
        curr = dummy

        while heap:
            value, i, node = heapq.heappop(heap)

            curr.next = node
            curr = node

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
