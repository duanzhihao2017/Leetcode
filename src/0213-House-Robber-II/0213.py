# 213. House Robber II
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
#
# Example 1:
#
# Input: [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
#              because they are adjacent houses.
# Example 2:
#
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) > 0:
            pre11, pre12, pre21, pre22 = 0, 0, 0, 0
            for i in nums[:-1]:
                pre11, pre12 = pre12, max(pre11 + i, pre12)
            for i in nums[1:]:
                pre21, pre22 = pre22, max(pre21 + i, pre22)
        else:
            return nums[0] if len(nums) == 0 else 0
        return max(pre12, pre22)

if __name__ == '__main__':
    nums = [2,3,2]
    print(Solution().rob(nums))