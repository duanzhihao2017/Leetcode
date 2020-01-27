class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """ 
        mem = dict()
        nums.sort()
        return self._combinationSum4(nums, target, mem)
        
    def _combinationSum4(self, nums, target, mem):
        if target == 0:
            return 1

        if target in mem:
            return mem[target]

        result = 0
        for num in nums:
            if num > target:
                break
            result += self._combinationSum4(nums, target - num, mem)

        mem[target] = result
        return result


class Solution2:
    def combinationSum4(self, nums, target):
        dp = [0] * (target + 1 )
        dp[0] = 1
        for i in range(1, target + 1):
            for j in nums:
                if i - j >= 0:
                    dp[i] += dp[i-j]
        return dp[-1]


if __name__ == '__main__':
    nums = [1, 2, 3]
    target = 4
    print(Solution().combinationSum4(nums, target))
    print(Solution2().combinationSum4(nums, target))
