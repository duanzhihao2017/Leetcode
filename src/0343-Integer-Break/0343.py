# 343. Integer Break
# Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.
#
# Example 1:
#
# Input: 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.
# Example 2:
#
# Input: 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
# Note: You may assume that n is not less than 2 and not larger than 58.

class Solution:
    def integerBreak_dp(self, n):
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * dp[i - j], j * (i - j))
        return dp[n]
    
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """  
        if n <= 3:
            return n - 1
        
        result = 1
        while n > 4:
            n -= 3
            result *= 3

        return n * result


if __name__ == '__main__':
    n = 4
    print(Solution().integerBreak_dp(n))
    print(Solution().integerBreak(n))
    n = 10
    print(Solution().integerBreak_dp(n))
    print(Solution().integerBreak(n))



    a=[1,2]
    hash(a)
    a=(1,2)
    hash(1,2)
    a=[(1,2),(2,3)]
