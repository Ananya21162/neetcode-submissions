class Solution:
    def findCodes(self,i,n,s,dict_code,ans):
        if i == n:
            ans[0] += 1
            return
        for j in range(i, i+3):
            ss = s[i:j+1]
            # print(ss)
            if ss not in dict_code:
                return
            # sub.append(dict_code[ss])
            self.findCodes(j+1,n,s,dict_code,ans)
            # sub.pop()
        # self.findCodes(n,n,s,dict_code,ans)
    def numDecodings(self, s: str) -> int:
        dict_code = { str(i) for i in range(1,27)}

        ans = [0]
        self.findCodes(0,len(s),s,dict_code,ans)
        return ans[0]