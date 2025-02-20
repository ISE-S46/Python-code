class Solution(object):
    def lengthOfLastWord(self, s):
        length = s.split()
        return len(length[-1])

word = input("Enter word 1 : ")
func = Solution()
value = func.lengthOfLastWord(word)
print(value)