class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        premap={i:[] for i in range(numCourses)}

        for crs, pre in  prerequisites:
            premap[crs].append(pre)

        visited= set()
        cycle=set()

        def dfs(course):
            if course in cycle:
                return False

            if course in visited:
                return True

            cycle.add(course)

            for pre in premap[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            visited.add(course)
            return True


        for i in range(numCourses):
            if not dfs(i):
                return False

        return True


        