class Solution(object):
    def repeatedSubstringPattern(self, s):
        return (s + s).find(s, 1) != len(s)

word = input("Enter word 1 : ")
func = Solution()
value = func.repeatedSubstringPattern(word)
print(value)