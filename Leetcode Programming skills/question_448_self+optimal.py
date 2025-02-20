class Solution(object):
    def findDisappearedNumbers(self, nums):
        sol = set(range(1, len(nums)+1)) - set(nums)
        res = list(sol)
        return res

input = list(map(int, input("Enter numbers separated by space: ").split()))
func = Solution()
value = func.findDisappearedNumbers(input)
print(value)