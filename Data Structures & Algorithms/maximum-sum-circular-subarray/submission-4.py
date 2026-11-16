class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        rightmax = [0]*n
        suffixSum = [0]*n
        
        for i in range(n-2,-1,-1):
            suffixSum[i] = suffixSum[i+1]+nums[i+1]
            rightmax[i] = max(suffixSum[i],rightmax[i+1])

        prefixSum = [nums[0]]*n
        maxSum = max(nums[0],nums[0]+rightmax[0])
        currmax = 0
        for i in range(1,n):
            prefixSum[i] = prefixSum[i-1]+nums[i]
            if currmax < 0:
                currmax = 0
            currmax += nums[i]
            maxSum = max(maxSum,rightmax[i]+prefixSum[i],nums[i],prefixSum[i],currmax)
        print(rightmax,prefixSum)
        return maxSum