# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 考慮輸入的list是空元素或者只有一個元素 (兩個if)
        if not head:
            return
        if head.next == None:
            return head

        # 定義三個位置指針
        prev = None
        curr = head
        after = head.next

        # 如果after指針還沒達到None，三個位置指針分別往前動
        while after:
            curr.next = prev
            prev = curr
            curr = after
            after = after.next

        # 當after最終移到None之後，curr目前的指針要重新讓他指向前一個
        curr.next = prev
        return curr