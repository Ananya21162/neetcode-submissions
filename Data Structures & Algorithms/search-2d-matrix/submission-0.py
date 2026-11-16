class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N, M = len(matrix), len(matrix[0])
        for i in range(N):
            first , last = matrix[i][0], matrix[i][-1]
            if target >= first and target <= last:
                l, r = 0, M-1
                while l <= r:
                    mid = (l+r) // 2
                    value = matrix[i][mid]
                    if value == target:
                        return True
                    elif value > target:
                        r = mid-1
                    else:
                        l = mid+1
        return False