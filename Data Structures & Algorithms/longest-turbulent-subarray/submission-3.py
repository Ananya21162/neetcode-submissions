class Solution:
    def isTurbulent(self,l,r,arr):
        if r-l+1 < 2:
            return True
        if r-l+1 == 2:
            if arr[l] == arr[r]:
                return False
            return True
        # compare last three indices
        k = r-1
        first = arr[k]- arr[k-1]
        second = arr[k+1]-arr[k]
        if (first > 0 and second < 0) or (first < 0 and second > 0):
            return True
        else:
            return False

    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r = 0, 0
        n = len(arr)
        maxT = 0
        while l <=r and r < n:
            if self.isTurbulent(l,r,arr):
                maxT = max(maxT, r-l+1)
                print(maxT)
                r += 1
            else:
                l += 1
        return maxT
