class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        if len(temperatures) <=1: return len(temperatures)

        stack=[]

        result= [0]* len(temperatures)


        for i in range(len(temperatures)):

           
            while stack and  temperatures[stack[-1]] < temperatures[i]:
                ind= stack[-1]
                result[ind] = i - ind
                stack.pop()

            stack.append(i)


        return result

        




        

        