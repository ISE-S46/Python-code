class Solution(object):
    def largestPerimeter(self, nums):
        nums = sorted(nums)[::-1]
        for i in range(len(nums) - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0

input = list(map(int, input("Enter numbers separated by space: ").split()))
func = Solution()
value = func.largestPerimeter(input)
print(value)