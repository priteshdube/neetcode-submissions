class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        premap={i:[] for i in range(numCourses)}

        for crs, pre in  prerequisites:
            premap[crs].append(pre)

        visit= set()

        def dfs(course):
            if course in visit:
                return False

            if premap[course]==[]:
                return True

            visit.add(course)

            for pre in premap[course]:
                if not dfs(pre):
                    return False
            visit.remove(course)
            premap[course]= []
            return True


        for i in range(numCourses):
            if not dfs(i):
                return False

        return True


        