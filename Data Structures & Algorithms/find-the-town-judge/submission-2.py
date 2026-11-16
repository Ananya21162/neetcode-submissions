class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inOut = defaultdict(int)

        for a,b in trust:
            if a !=b:
                inOut[a] -= 1
                inOut[b] += 1

        for key, value in inOut.items():
            if value == n-1:
                return key
        return -1


