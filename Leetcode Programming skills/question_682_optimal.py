class Solution(object):
    def calPoints(self, operations):
        record = []
        for op in operations:
            if op == 'D':
                record.append(record[-1]*2)
            elif op == 'C':
                record.pop()
            elif op == '+':
                record.append(record[-1]+record[-2])
            else:
                record.append(int(op))
        return sum(record)

input = list(input("Enter array value separated by space: ").split())
func = Solution()
value = func.calPoints(input)
print(value)