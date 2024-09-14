"""
Merge K Sorted Linked Lists
You are given an array of k linked lists lists, 
where each list is sorted in ascending order.

Return the sorted linked list that is the 
result of merging all of the individual linked lists.
Input: lists = [[1,2,4],[1,3,5],[3,6]]

Output: [1,1,2,3,3,4,5,6]

Input: lists = []

Output: []

Input: lists = [[]]

Output: []
"""

from typing import List, Optional
import heapq


# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        while len(lists) > 1:  # keep sorting until we have only one list
            mergedList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedList.append(self.mergeLists(l1, l2))
            lists = mergedList
        return lists[0]

    def mergeLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            short = l1
            big = l2
        else:
            short = l2
            big = l1

        short.next = self.mergeLists(short.next, big)
        return short


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


# Helper function to convert a list of lists into a list of linked lists
def create_list_of_linked_lists(list_of_values):
    return [create_linked_list(values) for values in list_of_values]


# Example usage
if __name__ == "__main__":
    # Example 1
    input_lists1 = [[1, 2, 4], [1, 3, 5], [3, 6]]
    linked_lists1 = create_list_of_linked_lists(input_lists1)

    print("Linked lists for Example 1:")
    for idx, ll in enumerate(linked_lists1):
        print(f"List {idx}: ", end="")
        print_linked_list(ll)

    # Merge the k sorted linked lists using the Solution class
    solution = Solution()
    merged_head1 = solution.mergeKLists(linked_lists1)

    # Print the merged linked list
    print("\nMerged linked list (Example 1):")
    print_linked_list(merged_head1)

    # Example 2: Empty input
    input_lists2 = []
    linked_lists2 = create_list_of_linked_lists(input_lists2)

    print("\nLinked lists for Example 2 (empty input):")
    for idx, ll in enumerate(linked_lists2):
        print(f"List {idx}: ", end="")
        print_linked_list(ll)

    merged_head2 = solution.mergeKLists(linked_lists2)

    print("\nMerged linked list (Example 2):")
    print_linked_list(merged_head2)

    # Example 3: List of empty lists
    input_lists3 = [[]]
    linked_lists3 = create_list_of_linked_lists(input_lists3)

    print("\nLinked lists for Example 3 (list of empty lists):")
    for idx, ll in enumerate(linked_lists3):
        print(f"List {idx}: ", end="")
        print_linked_list(ll)

    merged_head3 = solution.mergeKLists(linked_lists3)

    print("\nMerged linked list (Example 3):")
    print_linked_list(merged_head3)
