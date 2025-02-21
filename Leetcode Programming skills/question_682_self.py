class Solution(object):
    def calPoints(self, operations):
        new = []
        count = 0
        for i in range(len(operations)):
            try:
                new.append(int(operations[i]))
            except:
                new.append(operations[i])

            if (new[count] == "C"):
                new.remove(new[count])
                new.remove(new[count-1])
                count -= 2
            elif (new[count] == "D"):
                new.remove(new[count])
                new.append(new[count-1] * 2)
            elif (new[count] == "+"):
                new.remove(new[count])
                new.append(new[count-1] + new[count-2])
            
            count += 1
        
        return sum(new)
        

input = list(input("Enter array value separated by space: ").split())
func = Solution()
value = func.calPoints(input)
print(value)