class Solution(object):
    def countOdds(self, low, high):
        if low % 2 != 0 or high % 2 != 0:
            return ((high-low)/2)+1
        else:
            return (high-low)/2
        
input1 = 3
input2 = 7
func = Solution()
value = func.countOdds(input1, input2)
print(value)