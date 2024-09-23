"""
Find Median in a Data Stream

The median is the middle value in a sorted list of integers. 
For lists of even length, there is no middle value, 
so the median is the mean of the two middle values.

For example:

For arr = [1,2,3], the median is 2.
For arr = [1,2], the median is (1 + 2) / 2 = 1.5
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far.
Example 1:

Input:
["MedianFinder", "addNum", "1", "findMedian", "addNum", "3" "findMedian", "addNum", "2", "findMedian"]

Output:
[null, null, 1.0, null, 2.0, null, 2.0]

Explanation:
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.findMedian(); // return 1.0
medianFinder.addNum(3);    // arr = [1, 3]
medianFinder.findMedian(); // return 2.0
medianFinder.addNum(2);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

"""

import heapq


class MedianFinder:

    def __init__(self):
        self.small_nums = []  # Max heap
        self.large_nums = []  # Min Heap

    def addNum(self, num: int) -> None:
        # make sure every element is large is less than every in small
        if len(self.large_nums) and num < self.large_nums[0]:
            heapq.heappush(self.small_nums, -1 * num)
        else:
            heapq.heappush(self.large_nums, num)

        # Make sure they are approximately equal, not more than 1
        if len(self.small_nums) > len(self.large_nums) + 1:
            # pop from small and add to large
            val = -1 * heapq.heappop(self.small_nums)
            heapq.heappush(self.large_nums, val)
        if len(self.large_nums) > len(self.small_nums) + 1:
            val = heapq.heappop(self.large_nums)
            heapq.heappush(self.small_nums, -1 * val)

    def findMedian(self) -> float:
        if len(self.small_nums) > len(self.large_nums):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2.0


# Example usage
if __name__ == "__main__":
    medianFinder = MedianFinder()
    medianFinder.addNum(1)
    print("Current Median:", medianFinder.findMedian())  # Should return 1.0
    medianFinder.addNum(3)
    print("Current Median:", medianFinder.findMedian())  # Should return 2.0
    medianFinder.addNum(2)
    print("Current Median:", medianFinder.findMedian())  # Should return 2.0
