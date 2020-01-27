class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                result += prices[i+1] - prices[i]

        return result

class Solution(object):
    def maxProfit(self, prices):
        if prices == []:
            return 0
        min = prices[0]
        ans = 0
        arr = []
        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
            arr.append(prices[i]-min)
            min = prices[i]
        return sum(arr)

if __name__ == "__main__":
    prices = [1,2,3,4,5]
    print(Solution().maxProfit(prices))