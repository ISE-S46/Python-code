class Solution(object):
    def findTheDifference(self, s, t):
        for i in t:
            if t.count(i)>s.count(i):
                return(i)
                break

word1 = input("Enter word 1 : ")
word2 = input("Enter word 2 : ")
Function_find_diff = Solution()
Added_word = Function_find_diff.findTheDifference(word1, word2)
print(Added_word)