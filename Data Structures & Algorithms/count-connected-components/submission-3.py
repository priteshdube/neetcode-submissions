class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges: return 0 


        adjlist= defaultdict(list)

        for n1,n2 in edges:
            adjlist[n1].append(n2)
            adjlist[n2].append(n1)

        visited= set()

        def dfs(node):

            if node in visited: 
                return 

            visited.add(node)

            for nei in adjlist[node]:
                dfs(nei)


            
            

        count = 0

        for i in range(n):
            if i not in visited:
                dfs(i)
                count +=1

        return count

            


        