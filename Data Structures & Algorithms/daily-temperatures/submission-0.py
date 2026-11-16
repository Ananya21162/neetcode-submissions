class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0]
        stack = [(temperatures[n-1],n-1)]
        for i in range(n-2,-1,-1):
            curr = temperatures[i]
            while stack and stack[-1][0] <= curr:
                stack.pop()
            if not stack:
                ans.append(0)
            else:
                ans.append(stack[-1][1]-i)
            stack.append((curr,i))
        return ans[::-1]
