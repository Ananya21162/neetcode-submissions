class Solution:
    def trap(self, height: List[int]) -> int:
        left,right = [0], [0]
        for i in range(len(height)):
            left.append(max(left[-1],height[i]))
       
        for i in range(len(height)-1,-1,-1):
            right.append(max(right[-1],height[i]))
          
        right = right[::-1]
        # print(left,right)
        ans = 0
        for i in range(len(height)):
            h = min(left[i],right[i])
            if h > height[i]:
                ans += (h-height[i])
        return ans