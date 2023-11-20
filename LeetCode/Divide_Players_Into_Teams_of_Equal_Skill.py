class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l,r = 0, len(skill) -1
        prev = skill[l] + skill[r]
        ans = 0
        while l<r:
            chemistry = skill[l] * skill[r]
            total_skill = skill[l] + skill[r]
            if total_skill != prev:
                return -1
            ans +=chemistry
            l+=1
            r-=1
        return ans
