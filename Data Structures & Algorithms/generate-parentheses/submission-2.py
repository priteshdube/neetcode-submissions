class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result= []

        def helper(temp,open_br, close_br):
            if close_br == close_br == n:
                result.append("".join(temp[:]))
                return 

            if open_br > n:
                return

            
           
            helper(temp+ ["("], open_br+1, close_br)
    
            if close_br < open_br:
                helper(temp +[")"], open_br, close_br+1)

        helper([], 0, 0)

        return result

    


            

            

        

        
        