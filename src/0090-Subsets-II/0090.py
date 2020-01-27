class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = list()
        self._subsetsWithDup(nums, 0, list(), result)
        return result
    
    def _subsetsWithDup(self, nums, index, path, result):
        result.append(path.copy())
        for i in range(index, len(nums)):
            if index < i and nums[i] == nums[i - 1]:# add
                continue
            self._subsetsWithDup(nums, i + 1, path + [nums[i]], result)


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        r = [[]]
        for num in nums:
            r += [sorted(x + [num]) for x in r]
        r = list(set(tuple(x) for x in r))
        return r

if __name__ == '__main__':
    nums = [1, 2, 2]
    print(Solution().subsetsWithDup(nums))