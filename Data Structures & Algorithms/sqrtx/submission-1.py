class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        l, r = 1, x //2
        ans = 1
        while l <= r:
            mid = (l+r) // 2
            square = mid*mid
            if square <= x:
                ans = mid
                l = mid+1
            else:
                r = mid -1
        return ans