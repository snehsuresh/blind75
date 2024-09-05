"""
Merge Two Sorted Linked Lists
Solved 
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and 
return the head of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.

Input: list1 = [1,2,4], list2 = [1,3,5]

Output: [1,1,2,3,4,5]

"""

from typing import Optional


# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        # iterative
        # dummy = node = ListNode()
        # while list1 and list2:
        #     if list1.val < list2.val:
        #         node.next = list1.val
        #         list1 = list1.next
        #     else:
        #         node.next = list2.val
        #         list2 = list2.next
        #     node = node.next
        # node.next = list1 or list2

        # return dummy.next()

        # Recursive

        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val < list2.val:
            smallNode = list1
            bigNode = list2
        else:
            smallNode = list2
            bigNode = list1

        smallNode.next = self.mergeTwoLists(smallNode.next, bigNode)
        return smallNode


# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


# Helper function to print the linked list
def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    print(values)


# Example usage
if __name__ == "__main__":
    # Create two linked lists from lists of values
    list1_values = [1, 2, 4]
    list2_values = [1, 3, 5]
    list1 = create_linked_list(list1_values)
    list2 = create_linked_list(list2_values)

    # Print the original linked lists
    print("List 1:")
    print_linked_list(list1)

    print("List 2:")
    print_linked_list(list2)

    # Merge the two linked lists using the Solution class
    solution = Solution()
    merged_head = solution.mergeTwoLists(list1, list2)

    # Print the merged linked list
    print("Merged linked list:")
    print_linked_list(merged_head)
