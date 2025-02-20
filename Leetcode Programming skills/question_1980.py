class Solution(object):
    def findDifferentBinaryString(self, nums):
        missing = []
        for i in range(len(nums)):
            sub = [] * len(nums[0])
            for j in range(len(nums)):
                return
            subl = ''.join(sub)
            if subl in nums:
                continue
            else:
                missing.append(subl)
        return missing

input = list(input("Enter numbers separated by space: ").split())
func = Solution()
value = func.findDifferentBinaryString(input)
print(value)
