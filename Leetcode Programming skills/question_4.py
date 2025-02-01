class Solution(object):
    def isAnagram(self, s, t):
        if(len(s)!=len(t)):
                return False
        for i in s+t:
            if((s.count(i) == t.count(i)) == False):
                return False
            return True
    

word1 = input("Enter word 1 : ")
word2 = input("Enter word 2 : ")
Anagram = Solution()
value = Anagram.isAnagram(word1, word2)
print(value)