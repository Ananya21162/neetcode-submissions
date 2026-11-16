class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans +=str(len(s))
            ans +="#"
            ans += s
        return ans
    def decode(self, s: str) -> List[str]:
        ans = []
        l = ""
        i = 0
        while i < len(s):
            if s[i] != "#":
                l += s[i]
                i += 1
            else:
                st = s[i+1:i+1+int(l)]
                i = i+int(l)+1
                ans.append(st)
                l = ""
        return ans



