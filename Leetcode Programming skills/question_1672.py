class Solution(object):
    def maximumWealth(self, accounts):
        rich = []
        for i in accounts:
            rich.append(sum(i))
        
        return max(rich)

input = [[1,2,3],[3,2,1]]
func = Solution()
value = func.maximumWealth(input)
print(value)
