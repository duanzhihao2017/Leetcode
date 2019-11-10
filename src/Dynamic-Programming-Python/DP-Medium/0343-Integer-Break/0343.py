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