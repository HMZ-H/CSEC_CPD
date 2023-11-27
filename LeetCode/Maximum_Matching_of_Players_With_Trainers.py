class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        l, r = 0,0
        max_mat= 0
        while r < len(trainers) and l < len(players):
            if players[l] <= trainers[r]:
                max_mat +=1
                l +=1
                r+=1
            elif players[l] > trainers[r]:
                r +=1
        return max_mat
        
