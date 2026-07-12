class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        
        #so basically think like the speed is somewhere between the lowest and highest number of banananas in a pile. then search through binary search

        left = 1
        right = max(piles)

        speed = float('inf')

        def checkspeed(mid):
            
            total = 0

            for pile in piles:
                total += math.ceil(pile/mid)
            return total


        while left <=right:
            mid = (left + right)//2
            hours = checkspeed(mid)

            if hours > h:
                left = mid+1
            else:
                speed = min(speed, mid)
                right = mid -1

        return speed
            


        
       

