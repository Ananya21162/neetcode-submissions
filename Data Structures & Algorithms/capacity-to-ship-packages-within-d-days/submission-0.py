class Solution:
    def canShip(self, cap,weights,days):
        count, currCap = 1, cap
        for w in weights:
            if currCap-w < 0:
                count += 1
                if count > days:
                    return False
                currCap = cap
            currCap -= w
        return True
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        ans = sum(weights)
        while l <= r:
            mid = (l+r) // 2
            if self.canShip(mid,weights,days):
                ans = min(ans,mid)
                r = mid-1
            else:
                l = mid+1
        return ans