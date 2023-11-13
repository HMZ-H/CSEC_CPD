class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # lis = set(nums)
        # nums.clear()
        # for i in lis:
        #     nums.append(i)
        # nums.sort()
         
        # return len(nums)
        i = 0
        for num in nums:
            if i == 0 or nums[i-1] != num:
                nums[i] = num
                i += 1
        return i
        
