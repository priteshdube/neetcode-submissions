class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        visit = set()

        mincost  = 0

        heap=[(0, points[0])]

        while heap:

            el= heapq.heappop(heap)
            dist = el[0]

            x1, y1 = el[1]

            if (x1,y1) in visit:
                continue

            mincost += dist
            visit.add((x1,y1))

            
            for i in range(len(points)):  
            
                x2, y2 = points[i]

                if (x2, y2) not in visit:

                    dist = abs(x2-x1) + abs(y2-y1)

                    heapq.heappush(heap, (dist, points[i]))

            
        return mincost



        