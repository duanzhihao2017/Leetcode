#276. Paint Fence
#There is a fence with n posts, each post can be painted with one of the k colors.
#
#You have to paint all the posts such that no more than two adjacent fence posts have the same color.
#
#Return the total number of ways you can paint the fence.
#
#Note: n and k are non-negative integers.
class Solution:
    def paintfence(self, posts, colors):
        dp = [0] * posts
        dp[0] = colors
        dp[1] = colors * colors
        for i in range(2, posts):
             dp[i] = (colors-1)*(dp[i-1] + dp[i-2])
        return dp[-1]
print Solution().paintfence(3,2)
            