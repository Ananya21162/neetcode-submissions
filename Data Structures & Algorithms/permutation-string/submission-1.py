class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 1. create freq maps for s1
        # 2. Iterate through s2 and keep a freq map for elements in range [l,r]
        # range: [l,r] >> which has all elements of s1
        # compare the freq map with s1 if it completely m,atches return True
        # if not, move l and update the freq map and recheck
        f_s1 = {}
        for ch in s1:
            f_s1[ch] = f_s1.get(ch,0)+1
        f_s2 = {}
        l, r = 0,0
        while r < len(s2):
            f_s2[s2[r]] = f_s2.get(s2[r],0)+1
            # match it with f_s1
            if s2[r] not in f_s1:
                # remove s2[r] 
                r += 1
                while l != r:
                    f_s2[s2[l]] -= 1
                    if f_s2[s2[l]] == 0:
                        del f_s2[s2[l]]
                    l += 1
            else:
                if f_s2[s2[r]] <= f_s1[s2[r]]:
                    r += 1
                else:
                    while f_s2[s2[r]] > f_s1[s2[r]]:
                        f_s2[s2[l]] -= 1
                        if f_s2[s2[l]] == 0:
                            del f_s2[s2[l]]
                        l += 1
                    r += 1
            # after adjustment match the f_s2 with fs1
            match = True
            for key, value in f_s1.items():
                if key not in f_s2 or f_s2[key] != value:
                    match = False
                    break
            if match:
                return True
        return False
                

