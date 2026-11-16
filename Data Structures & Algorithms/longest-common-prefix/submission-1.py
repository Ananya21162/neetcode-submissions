class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = list(strs[0])
        for i in range(1,len(strs)):
            s = list(strs[i])
            l, r = 0, 0
            while l < len(common) and r < len(strs[i]):
                if common[l] == strs[i][r]:
                    l += 1
                    r += 1
                else:
                    break
            common = common[:l]
        return "".join(common)