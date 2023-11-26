class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        l, r = 0, len(nums)-1
        nums.sort()
        max_op = 0
        while l < r:
            current_sum = nums[l] + nums[r] 
            if  current_sum <= k:
                l +=1
            if current_sum >= k:
                r -=1
            if current_sum == k:
                max_op +=1
            
        return max_op
