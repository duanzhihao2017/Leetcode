# 136. Single Number
# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
# Example 1:
#
# Input: [2,2,1]
# Output: 1
# Example 2:
#
# Input: [4,1,2,1,2]
# Output: 4


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for index, value in enumerate(nums):
            if index == 0:
                res = value
            else:
                res ^= value
        return res


class Solution2(object):
    def singleNumber(self, nums):

        n = len(nums)
        res = nums[0]
        for i in range(1, n):
            res ^= nums[i]
        return res


if __name__ == "__main__":
    nums = [4, 2, 2, 1, 1]
    print Solution().singleNumber(nums)