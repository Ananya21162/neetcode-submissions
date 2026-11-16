class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        maxH = 0
        while (l < r):
            maxH =  max(maxH, (r-l)*min(heights[l], heights[r]))
            if heights[r] < heights[l]:
                r = r - 1
            else:
                l += 1
        return maxH