class Solution(object):
    def plusOne(self, digits):
        integer = int("".join([str(x) for x in digits]))
        P_int = integer + 1
        return list(map(int, str(P_int)))

input = list(map(int, input("Enter numbers separated by space: ").split()))
func = Solution()
value = func.plusOne(input)
print(value)