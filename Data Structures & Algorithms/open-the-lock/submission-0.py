class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        q = deque(["0000"])
        deadends.add("0000")
        turns = 0
        while q:
            turns += 1  
            # print(curr)
            for _ in range(len(q)):
                curr = q.popleft()
               
                for i in range(4):
                    d1 = (int(curr[i])+1) % 10
                    d2 = (int(curr[i])-1+10)%10
                    n1, n2 = curr[:i]+str(d1)+curr[i+1:],curr[:i]+str(d2)+curr[i+1:]
                    if n1 == target or n2 == target:
                        return turns
                    if n1 not in deadends:
                        q.append(n1)
                        deadends.add(n1)
                    if n2 not in deadends:
                        q.append(n2)
                        deadends.add(n2)
                    
            
        return -1