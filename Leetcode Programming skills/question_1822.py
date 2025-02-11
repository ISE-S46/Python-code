class Solution(object):
    def arraySign(self, nums):
        res = 1
        for val in nums:
            res = res * val
        if(res>=1):
            return 1
        elif(res==0):
            return 0
        else:
            return -1

input = list(map(int, input("Enter numbers separated by space: ").split()))
func = Solution()
value = func.arraySign(input)
print(value)