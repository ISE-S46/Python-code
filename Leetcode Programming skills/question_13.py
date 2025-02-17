class Solution(object):
    def romanToInt(self, s):
        rome = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        s = s[::-1]
        val = 0
        for i,l in enumerate(s):
            if(val != 0 and rome.get(s[i-1]) > rome.get(s[i])):
                val -= rome.get(l)
            else:
                val += rome.get(l)
        return val


word = input("Enter word 1 : ")
func = Solution()
value = func.romanToInt(word)
print(value)