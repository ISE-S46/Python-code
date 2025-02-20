class Solution(object):
    def findDifferentBinaryString(self, nums):
        strSet = {str for str in nums}
        def backtrack(i, ele):
            if i == len(nums):
                res = ''.join(ele)
                return None if res in strSet else res

            res = backtrack(i+1, ele)
            if res: return res

            ele[i] = '1'
            res = backtrack(i+1, ele)
            if res: return res
        
        return backtrack(0, ["0" for e in nums])

input = list(input("Enter numbers separated by space: ").split())
func = Solution()
value = func.findDifferentBinaryString(input)
print(value)
