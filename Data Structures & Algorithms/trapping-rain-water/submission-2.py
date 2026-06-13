class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height)<=2: return 0 

        

        leftmax= [0] * len(height)
        leftmax[0] = height[0]

        for i in range(1, len(height)):

            leftmax[i] = max(leftmax[i-1], height[i])


        rightmax = [0]* len(height)
        rightmax[-1] = height[-1]

        for i in range(len(height)-2, -1, -1):
            rightmax[i]= max(rightmax[i+1], height[i])

        area= 0

        for i in range(len(height)):
           area += min(leftmax[i], rightmax[i]) - height[i]

        return area


        