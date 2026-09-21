class Solution:
    def maxArea(self, height: list[int]) -> int:
        # max_area = 0
        # for i in range(len(height)-1):
        #     for j in range(i+1,len(height)):
        #         w = j-i
        #         h = min(height[i],height[j])        # got TLE
        #         curr_area = w * h
        #         if curr_area > max_area:
        #             max_area = curr_area
        # return max_area
            

        left = 0
        right = len(height)-1
        max_area = 0
        while left < right:
            curr_area = (right-left) * min(height[right],height[left])
            if  curr_area > max_area:
                max_area = curr_area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
        return max_area

        