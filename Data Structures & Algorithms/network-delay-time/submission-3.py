class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adjlist = defaultdict(list)
        
        for ui, vi, ti in times:
            adjlist[ui].append((vi, ti))

        visit= set()
        heap = [(0,k)]

        t= 0

        while heap:
            time, node = heapq.heappop(heap)

            if node in visit:
                continue

            t = max(t, time)
            visit.add(node)

            for vi, ti in adjlist[node]:
                if vi not in visit:
                    heapq.heappush(heap, (time + ti,  vi ))

        return t if len(visit) ==n else -1

            

    

        