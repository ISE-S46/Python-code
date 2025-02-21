class Solution(object):
    def test(self, nums):
        permu = []
        sol = []
        def backtrack():
            if len(nums) == len(sol):
                permu.append(sol[:])
                return
            
            for i in nums:
                if i not in sol:
                    sol.append(i)
                    backtrack()
                    sol.pop()

        backtrack()
        return permu

input = list(map(int, input("Enter numbers separated by space: ").split()))
func = Solution()
value = func.test(input)
print(value)