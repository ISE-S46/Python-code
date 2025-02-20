class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        if n not in nums: return n
        for i in range(n):
            if i not in nums:
                return i

input = list(map(int, input("Enter numbers separated by space: ").split()))
func = Solution()
value = func.missingNumber(input)
print(value)