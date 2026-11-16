class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        isZero = 0
        totalP = 1
        for num in nums:
            if num == 0:
                isZero += 1
            else:
                totalP *= num
        ans = []
        for num in nums:
            if isZero == 1:
                if num == 0:
                    ans.append(totalP)
                else:
                    ans.append(0)
            elif isZero > 1:
                ans.append(0)
            else:
                ans.append(totalP//num)
        return ans