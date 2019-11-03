class Solution:
    def nthUglyNumber(self, n):
        ans = [1] * n
        a = b = c = 0
        for i in range(1, n):
            ans[i] = min(ans[a]*2, ans[b]*3,ans[c]*5)
            if ans[a]*2 == ans[i]: a += 1
            if ans[b]*3 == ans[i]: b += 1
            if ans[c]*5 == ans[i]: c += 1
        return ans[-1]

if __name__ == '__main__':
    print Solution().nthUglyNumber(10)
