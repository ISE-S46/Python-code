class Solution(object):
    def findDifferentBinaryString(self, nums):
        n = len(nums)
        res = []
        sol = []
        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return
            backtrack(i+1)

            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
        
        backtrack(0)
        return res

input = list(map(int, input("Enter numbers separated by space: ").split()))
func = Solution()
value = func.findDifferentBinaryString(input)
print(value)
