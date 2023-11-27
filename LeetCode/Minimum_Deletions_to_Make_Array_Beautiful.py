class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        n = len(nums)
        delete = count= 0
        for i in range(n-1):
            if (count%2) ==0 and (nums[i] == nums[i + 1]):
                delete +=1
            else:
                count +=1
        count +=1
        delete += count & 1
        return delete
