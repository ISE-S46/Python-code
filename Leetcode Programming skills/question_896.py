class Solution(object):
    def isMonotonic(self, nums):
        In = 0
        De = 0
        for i in range(len(nums)-1):
            if(nums[i] > nums[i+1]) and De == 0:
                In += 1
                continue
            elif(nums[i] < nums[i+1]) and In == 0:
                De += 1
                continue
            elif(nums[i] == nums[i+1]):
                continue
            else:
                return False
        return True

input = list(map(int, input("Enter numbers separated by space: ").split()))
func = Solution()
value = func.isMonotonic(input)
print(value)