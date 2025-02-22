class Solution(object):
    def judgeCircle(self, moves):
        x = 0
        y = 0
        for i in moves:
            if(i == "L"):
                x+= 1
            elif(i == "R"):
                x+= -1
            elif(i == "U"):
                y+= 1
            elif(i == "D"):
                y+= -1
        
        return [0,0] == [x, y]

input = list(input("Enter array value separated by space: ").split())
func = Solution()
value = func.judgeCircle(input)
print(value)