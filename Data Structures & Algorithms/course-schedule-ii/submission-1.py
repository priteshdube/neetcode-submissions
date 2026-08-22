class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        

        premap= defaultdict(list)

        for crs, pre in prerequisites:
            premap[crs].append(pre)

        cycle= set()

        visited= set()

        order=[]

        def dfs(crs):
            if crs in cycle:
                return False

            if crs in visited:
                return True

            cycle.add(crs)

            for pre in premap[crs]:
                if not dfs(pre):
                    return False

                
            cycle.remove(crs)
            order.append(crs)
            visited.add(crs)
            return True


        for cr in range(numCourses):
            if not dfs(cr):
                return []

        return order

        