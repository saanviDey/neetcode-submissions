class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSeen = collections.defaultdict(set)
        colSeen = collections.defaultdict(set)
        squareSeen = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    if (board[r][c] in rowSeen[r] or
                        board[r][c] in colSeen[c] or
                        board[r][c] in squareSeen[(r // 3, c // 3)]):

                        return False
                    
                    colSeen[c].add(board[r][c])
                    rowSeen[r].add(board[r][c])
                    squareSeen[(r//3,c//3)].add(board[r][c])
        
        return True

        