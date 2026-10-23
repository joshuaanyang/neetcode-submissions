class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxs = [set() for _ in range(9)]


        for r in range(9):
            for c in range(9):

                value = board[r][c]
                box_index = (r//3)*3+(c//3)
                if value == ".":
                    continue

                if value in rows[r] or value in cols[c] or value in boxs[box_index]  :
                    return False
                
                
                cols[c].add(value)
                boxs[box_index].add(value)
                rows[r].add(value)  
        return True


            

        