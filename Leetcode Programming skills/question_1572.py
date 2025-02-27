class Solution(object):
    def diagonalSum(self, mat):
        if len(mat) == 1:
            return mat[0][0]

        pri = [mat[i][i] for i in range(len(mat))]
        sec = [mat[i][len(mat)-i-1] for i in range(len(mat))]

        if pri[(len(pri)-1)/2] == sec[(len(sec)-1)/2] and len(mat) % 2 != 0:
            return sum(pri) + sum(sec) - pri[(len(pri)-1)/2]

        return sum(pri) + sum(sec)