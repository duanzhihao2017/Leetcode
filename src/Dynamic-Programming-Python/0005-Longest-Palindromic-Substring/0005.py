class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        index = 0
        result = ''
        while index < len(s):
            l = index 
            r = index 
            while r + 1 < len(s) and s[r] == s[r + 1]:
                r += 1 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if len(s[l+1:r]) > len(result):
                result = s[l+1:r]
            
            index += 1
        
        return result


if __name__ == "__main__":
    s = "babad"
    print(Solution().longestPalindrome(s))