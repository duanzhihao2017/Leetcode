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