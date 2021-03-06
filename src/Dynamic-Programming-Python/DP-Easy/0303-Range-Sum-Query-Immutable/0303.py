#303. Range Sum Query - Immutable
#Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
#
#Example: Given nums = [-2, 0, 3, -5, 2, -1]
#
#sumRange(0, 2) -> 1 sumRange(2, 5) -> -1 sumRange(0, 5) -> -3 Note: You may assume that the array does not change. There are many calls to sumRange function.

class NumArray:

    def __init__(self, nums):

        self.result = [0]*(len(nums)+1)
        
        for i in range(len(nums)):
            self.result[i+1] = self.result[i] + nums[i]

    def sumRange(self, i, j):
        return self.result[j+1] - self.result[i]
    
if __name__ == "__main__":
    print NumArray([-2, 0, 3, -5, 2, -1]).sumRange(2,5)