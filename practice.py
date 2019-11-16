# def integerBreak(n):
#
#     dp = [1]* (n+1)
#     for i in range(2, n+1):
#         for j in range(i):
#             dp[i] = max(dp[i-j]*j, (i-j)*j, dp[i])
#     return dp[n]
#
# print integerBreak(2)
#
#
# def lengthOfLIS(nums):
#     dp = [1] * len(nums)
#     for i in range(len(nums)):
#         for j in range(i):
#             if nums[j] > nums[i]:
#                 dp[i] = max(dp[j]+1, dp[i])
#     return dp
#
# print lengthOfLIS([10,9,2,5,3,7,101,18])