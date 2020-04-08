# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        arr = []
        temp = head
        while(temp):
            arr.append(temp)
            temp = temp.next
            n = len(arr)//2
        return arr[n]
        
