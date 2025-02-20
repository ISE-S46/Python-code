class Solution(object):
    def findDifferentBinaryString(self, nums):
        result = ""
        
        for i,n in enumerate(nums):
            if n[i] == "0":
                result += "1"
            else:
                result += "0"
        return result


input = list(input("Enter numbers separated by space: ").split())
func = Solution()
value = func.findDifferentBinaryString(input)
print(value)