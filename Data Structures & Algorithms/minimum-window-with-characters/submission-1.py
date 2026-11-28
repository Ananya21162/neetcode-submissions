class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window, countT = {}, {}
        for ch in t:
            countT[ch] = countT.get(ch,0)+1

        need = len(countT)
        have = 0
        res = ""
        lenR = float('inf')
        l = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r],0)+1
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            while have == need:
                if r-l+1 < lenR:
                    res = s[l:r+1]
                    lenR = r-l+1
                if s[l] not in countT.keys() or window[s[l]] > countT[s[l]]:
                    window[s[l]] -= 1
                    l += 1
                else: 
                    break
        return res
