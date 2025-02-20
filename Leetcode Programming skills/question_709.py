class Solution(object):
    def toLowerCase(self, s):
        Word = {
            "A" : "a",
            "B" : "b",
            "C" : "c",
            "D" : "d",
            "E" : "e",
            "F" : "f",
            "G" : "g",
            "H" : "h",
            "I" : "i",
            "J" : "j",
            "K" : "k",
            "L" : "l",
            "M" : "m",
            "N" : "n",
            "O" : "o",
            "P" : "p",
            "Q" : "q",
            "R" : "r",
            "S" : "s",
            "T" : "t",
            "U" : "u",
            "V" : "v",
            "W" : "w",
            "X" : "x",
            "Y" : "y",
            "Z" : "z",
        }
        smol = []
        for i in range(len(s)):
            if(s[i] in Word):
                smol.append(Word.get(s[i]))
            else:
                smol.append(s[i])
        return ''.join(smol)

word = input("Enter word 1 : ")
func = Solution()
value = func.toLowerCase(word)
print(value)