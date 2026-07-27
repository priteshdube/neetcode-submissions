class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        row = len(grid)
        col= len(grid[0])

        def helper(r,c):
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] != "1":
                return 

       

            grid[r][c]= "#"

            #four directions

            helper(r-1, c)
            helper(r+1, c)
            helper(r, c-1)
            helper(r, c+1)

        


        

          


        no_of_island = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    helper(r,c)
                    no_of_island += 1

        return no_of_island

        