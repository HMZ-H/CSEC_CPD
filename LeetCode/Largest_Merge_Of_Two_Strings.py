class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        p1, p2 = 0,0
        merge = ''
        while p1<len(word1) and p2<len(word2):
            if word1[p1] > word2[p2]:
                merge += word1[p1]
                p1+=1
            elif word1[p1] < word2[p2]:
                merge += word2[p2]
                p2+=1
            else:
                if word1[p1:] > word2[p2:]:
                    merge +=word1[p1]
                    p1+=1
                else:
                    merge +=word2[p2]
                    p2 +=1
        if p1<len(word1):
            merge += word1[p1:]
        if p2 < len(word2):
            merge += word2[p2:]
        return merge


            
            
