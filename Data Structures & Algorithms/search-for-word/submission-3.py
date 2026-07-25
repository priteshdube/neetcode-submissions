class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        row = len(board)
        col = len(board[0])

        visited= set()


        def path(i, r, c):

            if i == len(word):
                return True

            if r < 0 or r >= row or c < 0 or c >= col or (r,c) in visited or board[r][c] != word[i]:
                return False

            

            visited.add((r,c))
            #four direcion

            check= path(i+1, r-1, c) or path(i+1, r+1, c) or path(i+1, r, c-1) or path(i+1, r, c+1)
            visited.remove((r,c))
            return check
         

        for r in range(row):
                for c in range(col):
                    if board[r][c] == word[0]:
                        if path(0,r,c):
                            return True
                    

   
        return False

                    
        