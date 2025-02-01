class Solution(object):
    def strStr(self, haystack, needle):
        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1

word1 = input("Enter word 1 : ")
word2 = input("Enter word 2 : ")
find_str = Solution()
index_str = find_str.strStr(word1, word2)
print(index_str)