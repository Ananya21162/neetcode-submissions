class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        n = len(heights)
        l,r = 0, n-1
        while l < r:
            h = min(heights[l],heights[r])
            w = r-l
            ans = max(ans,w*h)
            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1
        return ans