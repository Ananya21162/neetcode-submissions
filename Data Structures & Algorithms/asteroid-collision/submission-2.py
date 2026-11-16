class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if not asteroids:
            return []
        ans = [asteroids[0]]
        for i in range(1,len(asteroids)):
            curr = asteroids[i]
            alive = True
            while ans and ans[-1] > 0 and curr < 0:
                if ans[-1] == abs(curr):
                    ans.pop()
                    alive = False
                    break
                elif ans[-1] < abs(curr):
                    ans.pop()
                    continue
                else:
                    alive = False
                    break

            if alive:
                ans.append(curr)
           
        return ans
