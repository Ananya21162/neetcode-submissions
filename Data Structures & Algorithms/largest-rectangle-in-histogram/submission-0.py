class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        leftLowest, rightLowest = [], []
        stack = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if not stack:
                leftLowest.append(-1)
            else:
                leftLowest.append(stack[-1])
            stack.append(i)
        stack = []
        for i in range(len(heights)-1,-1,-1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if not stack:
                rightLowest.append(len(heights))
            else:
                rightLowest.append(stack[-1])
            stack.append(i)
        # print(rightLowest, leftLowest)
        rightLowest = rightLowest[::-1]
        for i in range(len(heights)):
            maxArea = max(maxArea, heights[i]*(rightLowest[i]-leftLowest[i]-1))
        return maxArea