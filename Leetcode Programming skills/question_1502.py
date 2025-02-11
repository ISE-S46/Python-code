class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        try:
            i = 0
            arr.sort()
            while i <= len(arr):
                case1 = abs(arr[i] - arr[i+1])
                case2 = abs(arr[i+1] - arr[i+2])
                i += 1
                if (case1 != case2) == True:
                    return False
                else:
                    continue
            return True
        except:
            return True

input = list(map(int, input("Enter numbers separated by space: ").split()))
func = Solution()
value = func.canMakeArithmeticProgression(input)
print(value)