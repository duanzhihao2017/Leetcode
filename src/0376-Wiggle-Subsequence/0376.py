class Solution:
    def wiggleMaxLength(self, nums):
        size = len(nums)
        _pos, _neg = 1, 1
        for i in range(1, size):
            if nums[i - 1] < nums[i]:
                _neg = _pos + 1
            elif nums[i - 1] > nums[i]:
                _pos = _neg + 1

        return _neg if _pos < _neg else _pos


if __name__ == "__main__":
    nums = [1, 7, 4, 9, 2, 5]
    print Solution().wiggleMaxLength(nums)