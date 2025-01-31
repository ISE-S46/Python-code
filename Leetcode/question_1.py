class Solution(object):
    def mergeAlternately(self, word1, word2):
        Merge = []
        if range(len(word1) >= len(word2)):
            for i in range(len(word1)):
                if(i<len(word2)):
                    Merge.append(word1[i])
                    Merge.append(word2[i])
                else:
                    Merge.append(word1[i])
        else:
            for i in range(len(word2)):
                if(i<len(word1)):
                    Merge.append(word1[i])
                    Merge.append(word2[i])
                else:
                    Merge.append(word2[i])
        return ''.join(Merge)

word1 = input("Enter word 1 : ")
word2 = input("Enter word 2 : ")
Function_Merge_word = Solution()
Merge_word = Function_Merge_word.mergeAlternately(word1, word2)
print(Merge_word)
