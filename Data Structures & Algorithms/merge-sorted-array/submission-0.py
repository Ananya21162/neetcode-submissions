class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tmp =[]
        l, r = 0, 0
        while l < m and r < n:
            if nums1[l] <= nums2[r]:
                tmp.append(nums1[l])
                l += 1
            else:
                tmp.append(nums2[r])
                r += 1
        while l < m:
            tmp.append(nums1[l])
            l += 1
        while r < n:
            tmp.append(nums2[r])
            r += 1
        for i in range(m+n):
            nums1[i] = tmp[i]
        
