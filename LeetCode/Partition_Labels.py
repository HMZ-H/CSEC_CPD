class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_oc = {char: index for index, char in enumerate(s)}
        result = []
        start, end = 0,0
        for i , char in enumerate(s):
            last_ind = last_oc[char]
            end = max(end, last_ind)
            
            if i == end:
                result.append(i - start + 1)
                start = i + 1 
        return result
