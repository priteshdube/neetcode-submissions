class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        row = len(grid)
        col = len(grid[0])

        def helper(r,c):

            if r< 0 or r >= row or c < 0 or c >= col or grid[r][c] != 1:
                return 0

            grid[r][c]= 0

        

            return 1+ helper(r+1,c)+ helper(r-1,c) + helper(r, c+1) + helper(r, c-1)


        maxarea = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    area = helper(r, c)
                    maxarea = max(maxarea, area)

        return maxarea

       

            

        