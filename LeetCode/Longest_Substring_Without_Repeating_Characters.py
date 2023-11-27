class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,max_len = 0,0
        count = {}
        for r in range(len(s)):
            char = s[r]
            if char in count and count[char] >=l:
                l = count[char] +1
            else:
                max_len = max(max_len, r - l +1)
            count[char] = r
        return max_len


        
