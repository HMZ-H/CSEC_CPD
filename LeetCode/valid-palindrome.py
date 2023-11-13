class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''
        for c in s.lower():
            if c.isalpha() or c.isnumeric():
                s1 += c
        print(s1)

        # s = s1[::-1]
        # return True if s1==s else False
        l, r = 0, len(s1) - 1
        while l < r:
            if s1[l] != s1[r]:
                return False
            l += 1
            r -= 1
        return True
