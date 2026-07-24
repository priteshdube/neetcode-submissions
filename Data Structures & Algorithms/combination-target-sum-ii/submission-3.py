class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        result= []

        def helper(i, temp, cursum):
            if cursum==target:
                result.append(temp[:])
                return


            if cursum > target:
                return 

            for j in range(i, len(candidates)):

                if j>i and candidates[j]== candidates[j-1]:
                    continue
                    
                temp.append(candidates[j])        
                helper(j+1, temp, cursum+ candidates[j])
                temp.pop()

        helper(0, [], 0)

        return result
