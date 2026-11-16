class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque([0])
        farthest = 0
        n = len(s)
        if s[-1] == '1':
            return False
        while q:
            # print(q)
            idx = q.popleft()
            start = max(idx+minJump,farthest+1)
            for i in range(start, min(idx+maxJump+1, len(s))):
                if s[i] == '0':
                    q.append(i)
                if i == n-1:
                    return True
            farthest = idx+maxJump
        return False