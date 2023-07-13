class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            for k, v in Counter(row).items():
                if k !="." and v>=2:
                    return False
    
        for col in range(len(board)):
            cols = [board[row][col] for row in range(len(board[col]))]
            for k, v in Counter(cols).items():
                if k!="." and v>=2:
                    return False

        for i in range(3):
            for j in range(3):
                blocks = []
                for ii in range(3):
                    for jj in range(3):
                        blocks.append(board[3*i+ii][3*j+jj])
                for k, v in Counter(blocks).items():
                    if k!="." and v>=2:
                        return False

        return True