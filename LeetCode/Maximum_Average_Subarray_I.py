class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window  =  sum(nums[:k])
        max_avg = window/k
        l = 0
        while l < len(nums)-k:
            window = window - nums[l] + nums[l + k]
            max_avg = max(max_avg, window/k)
            l +=1
        
        return max_avg

#######################################################

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = sum(nums[:k])
        max_average =  window/k
        for i in range(len(nums) -k):
            window = window - nums[i] + nums[i+k]

            max_average = max(max_average, window/k)
        return max_average        
