#70. Climbing Stairs
#You are climbing a stair case. It takes n steps to reach to the top.
#
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
#Note: Given n will be a positive integer.
#
#Example 1:
#
#Input: 2 Output: 2 Explanation: There are two ways to climb to the top.
#
#1 step + 1 step
#2 steps Example 2:
#Input: 3 Output: 3 Explanation: There are three ways to climb to the top.
#
#1 step + 1 step + 1 step
#1 step + 2 steps
#2 steps + 1 step


class Solution:
    def climb(self, n):
        x, y = 0, 1
        while n > 0:
            x, y = y, x+y 
            n -= 1
        return y

if __name__ == '__main__':
    n = 3
    print(Solution().climb(n))