class Solution(object):
    def lemonadeChange(self, bills):
        f = 0
        t = 0
        for i in bills:
            if i == 20 and t == 0:
                f -= 3
            elif i == 20 and t >= 1:
                f -= 1
                t -= 1
            if i == 10:
                t += 1
                f -= 1
            if i == 5:
                f += 1
            if f < 0 or t < 0:
                return False
        return True

input = list(map(int, input("Enter numbers separated by space: ").split()))
func = Solution()
value = func.lemonadeChange(input)
print(value)