class Solution(object):
    def tictactoe(self, moves):
        board = [[0,0,0],
                 [0,0,0],
                 [0,0,0]]
        c = 0
        for m in moves:
            if c % 2 == 0:
                board[m[0]][m[1]] = "A"
            else:
                board[m[0]][m[1]] = "B"
            c += 1

        diag1 = [board[0][0], board[1][1], board[2][2]]
        diag2 = [board[2][0], board[1][1], board[0][2]]

        if diag1 == ["A","A","A"] or diag2 == ["A","A","A"]:
            return "A"
        elif diag1 == ["B","B","B"] or diag2 == ["B","B","B"]:
            return "B"

        colboard = [list(col) for col in zip(*board)]

        for i in range(len(board)):
            if board[i] == ["A","A","A"] or colboard[i] == ["A","A","A"]:
                return "A"
            elif board[i] == ["B","B","B"] or colboard[i] == ["B","B","B"]:
                return "B"
            
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"
        
input = [[2,2],[1,2],[2,1],[1,1],[2,0]]
func = Solution()
value = func.tictactoe(input)
print(value)