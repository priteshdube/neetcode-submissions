class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []

        def helper(i, temp, cur_sum):

            if cur_sum== target:
                result.append(temp[:])
                return

            if i >= len(nums) or cur_sum > target:
                return 

            # i have two choices at each step either to take that number or not take it

            temp.append(nums[i])
            helper(i, temp, cur_sum+ nums[i])

            temp.pop()
            helper(i+1, temp, cur_sum)


        helper(0, [], 0)

        return result 

