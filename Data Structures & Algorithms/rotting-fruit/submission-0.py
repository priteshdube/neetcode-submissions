class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        time = 0
        q = deque()

        row = len(grid)
        col = len(grid[0])

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh += 1

                if grid[r][c] == 2:
                    q.append([r, c])

        while q and fresh > 0:
            cl = len(q)
            for i in range(cl):
                r, c = q.popleft()

                directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

                for dr, dc in directions:
                    cr, cc = r + dr, c + dc

                    if cr < 0 or cr >= row or cc < 0 or cc >= col or grid[cr][cc] != 1:
                        continue
                    grid[cr][cc] = 2
                    fresh -=1
                    q.append([cr, cc])

                
            time +=1


        return time if fresh== 0 else -1

            
