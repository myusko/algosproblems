# Given the head of a sorted linked list,
# delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Input: head = [1,1,2]
# Output: [1,2]

# Input: head = [1,1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,4,4,4]
# Output: [1,2,3,4]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return None

        current_node = head

        # Iterating over all the available nodes
        while current_node and current_node.next:
            # Keep a node of the parent node
            # In case if the current_node and the parent node of the current_node have the same values
            temporary_node = current_node.next.next

            # If a value is equal, set a parent node of the current next node
            if current_node.val == current_node.next.val:
                current_node.next = temporary_node

            # Otherwise, just keep iterating over the LinkedList
            else:
                current_node = current_node.next
        return head
