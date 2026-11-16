class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        goal = n-1
        count = 0
        q = deque()
        q.append(0)
        while q:
            for _ in range(len(q)):
                idx = q.popleft()
                if idx >= goal:
                    return count
                for i in range(idx+1, idx+nums[idx]+1):
                    if q and q[-1] > i:
                        continue
                    q.append(i)
            count += 1
            
        