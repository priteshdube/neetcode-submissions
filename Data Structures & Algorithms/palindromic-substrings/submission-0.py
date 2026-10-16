class Solution:
    def countSubstrings(self, s: str) -> int:

        if len(s) <=1 : return 1

        def checkpalindrone(start, end):

            count = 0 

            while start>= 0 and end <= len(s)-1 and s[start] == s[end]:

                count +=1


                start -=1 
                end +=1

            return count 

            


        result = 0

    

        for i in range(len(s)):

            #odd

            start = end = i

            while start>= 0 and end <= len(s)-1 and s[start] == s[end]:
                result +=1


                start -= 1
                end += 1

            #even 

            start = i
            end = i+1

            while start>= 0 and end <= len(s)-1 and s[start] == s[end]:

                result +=1

                start -=1 
                end +=1


        return result



            
            
        