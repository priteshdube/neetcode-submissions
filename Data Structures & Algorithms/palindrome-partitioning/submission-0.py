class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def checkpalindrone(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start +=1
                end -=1 

            return True

        result = []
        def helper(temp, i ):
            if i== len(s):
                result.append(temp[:])
                return
            
            for j in range(i, len(s)):
                if checkpalindrone(i, j):
                    temp.append(s[i: j+1])
                    helper(temp, j+1)
                    temp.pop()

        helper([], 0)
        return result
                        

                
                
 



           
            
        



          

        

        

        

        



        