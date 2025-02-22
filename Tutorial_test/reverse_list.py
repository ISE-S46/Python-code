class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1r = int(''.join(str(x) for x in l1[::-1]))
        l2r = int(''.join(str(y) for y in l2[::-1]))
        val = l1r + l2r
        l3 = list(map(int, str(val)))
        return l3[::-1]

l1 = list(map(int, input("Enter numbers separated by space: ").split()))
l2 = list(map(int, input("Enter numbers separated by space: ").split()))
func = Solution()
value = func.addTwoNumbers(l1, l2)
print(value)