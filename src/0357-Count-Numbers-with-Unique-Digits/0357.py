# 357. Count Numbers with Unique Digits
# Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.
#
# Example:
#
# Input: 2
# Output: 91
# Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100,
#              excluding 11,22,33,44,55,66,77,88,99

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 1
        dp = [9]
        for i in range(9, 9-n+1, -1):
            dp += [dp[-1]*i]
        return sum(dp) + 1


if __name__ == "__main__":
    print Solution().countNumbersWithUniqueDigits(4)