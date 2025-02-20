class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        actual = 0
        real = n*(n+1)/2
        for i in nums:
            actual = actual + i
        return real - actual

input = list(map(int, input("Enter numbers separated by space: ").split()))
func = Solution()
value = func.missingNumber(input)
print(value)