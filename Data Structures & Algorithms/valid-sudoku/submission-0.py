class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            buf1 = [0]*9
            buf2 = [0]*9
            for j in range(9):
                if board[i][j] != ".":
                    if buf1[int(board[i][j])-1] == 0:
                        buf1[int(board[i][j])-1] = 1
                    else:
                        return False
                if board[j][i] != ".":
                    if buf2[int(board[j][i])-1] == 0:
                        buf2[int(board[j][i])-1] = 1
                    else:
                        return False
        for i in range(3):
            for j in range(3):
                buf3 = [0]*9
                if board[3*i+1-1][3*j+1-1] != ".":
                    buf3[int(board[3*i+1-1][3*j+1-1])-1] += 1
                if board[3*i+1-1][3*j+1] != ".":
                    buf3[int(board[3*i+1-1][3*j+1])-1] += 1
                if board[3*i+1-1][3*j+1+1] != ".":
                    buf3[int(board[3*i+1-1][3*j+1+1])-1] += 1
                if board[3*i+1][3*j+1-1] != ".":
                    buf3[int(board[3*i+1][3*j+1-1])-1] += 1
                if board[3*i+1][3*j+1] != ".":
                    buf3[int(board[3*i+1][3*j+1])-1] += 1
                if board[3*i+1][3*j+1+1] != ".":
                    buf3[int(board[3*i+1][3*j+1+1])-1] += 1
                if board[3*i+1+1][3*j+1-1] != ".":
                    buf3[int(board[3*i+1+1][3*j+1-1])-1] += 1
                if board[3*i+1+1][3*j+1] != ".":
                    buf3[int(board[3*i+1+1][3*j+1])-1] += 1
                if board[3*i+1+1][3*j+1+1] != ".":
                    buf3[int(board[3*i+1+1][3*j+1+1])-1] += 1
                for i in buf3:
                    if i > 1:
                        return False
        return True

