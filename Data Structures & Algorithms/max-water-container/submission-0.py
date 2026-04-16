class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        right = n-1
        left=0
        min_diff=999999
        max_amnt=0
        while left < right:
            current_amnt = min(heights[left],heights[right])*(right - left)
            max_amnt=max(current_amnt,max_amnt)
            if heights[left] < heights[right]: 
                left+=1
            else: right-=1
        return max_amnt
            
        