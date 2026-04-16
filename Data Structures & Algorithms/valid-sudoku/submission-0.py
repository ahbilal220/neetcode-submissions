class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict= defaultdict(int)
        for i in range(9):
            row_dict.clear()
            for j in range(9):
                if board[i][j] != ".":
                    row_dict[board[i][j]]+=1
                    if row_dict[board[i][j]] > 1: return False

        col_dict=defaultdict(int)
        for i in range(9):
            col_dict.clear()
            for j in range(9):
                if board[j][i] != ".":
                    col_dict[board[j][i]]+=1
                    if col_dict[board[j][i]] > 1: return False
        
        for sq in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (sq // 3) * 3 +i
                    col = (sq % 3) * 3 +j

                    if board[row][col] == ".": continue
                    if board[row][col] in seen: return False
                    seen.add(board[row][col])
        return True
                