class Solution(object):
    def judgeCircle(self, moves):
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')

input = list(input("Enter array value separated by space: ").split())
func = Solution()
value = func.judgeCircle(input)
print(value)