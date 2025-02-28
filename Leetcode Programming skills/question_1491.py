class Solution(object):
    def average(self, salary):
        salary.remove(max(salary))
        salary.remove(min(salary))

        return float(sum(salary))/float(len(salary))

input = list(map(int, input("Enter numbers separated by space: ").split()))
func = Solution()
value = func.average(input)
print(value)