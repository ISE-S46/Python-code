class Solution(object):
    def moveZeroes(self, nums):
        j = 0
        i = 0
        try:
            nums.index(0)
            for u in range(len(nums)):
                if(nums[u] == 0):
                    j += 1
            while i < j:
                nums.remove(0)
                i+=1
            for v in range(j):
                nums.append(0)
            return nums
        except:
            return nums

input = list(map(int, input("Enter numbers separated by space: ").split()))
func = Solution()
value = func.moveZeroes(input)
print(value)