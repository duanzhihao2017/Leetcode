# 78. Subsets
# Given a set of distinct integers, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(index, tmp):
            res.append(tmp)
            for pos in range(index, len(nums)):
                dfs(pos+1, tmp + [nums[pos]])
            return res
        res = []
        dfs(0, [])
        return res


# class Solution:
#     def subsets(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         if not nums:
#             return [[]]
#         result = self.subsets(nums[1:])
#         return result + [[nums[0]] + s for s in result]


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().subsets(nums))