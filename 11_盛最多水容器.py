# 双指针，向内移动较小的边
class Solution:
    def maxArea(self, height) -> int:
        if not height or len(height)< 2:
            return 0
        max_vol = 0
        i,j = 0,len(height)-1
        while(i < j):
            max_vol = max(max_vol,min(height[i],height[j])*(j-i))
            if height[i] < height[j]:
                i +=1 
            else:
                j -= 1    
        return max_vol