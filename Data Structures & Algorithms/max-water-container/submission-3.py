class Solution:
    def maxArea(self, heights: List[int]) -> int:

        MA=0

        l,r=0,len(heights)-1

        while l<r:
            Area=min(heights[l],heights[r])*(r-l)
            MA=max(MA,Area)

            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return MA

            
            




            

       




        