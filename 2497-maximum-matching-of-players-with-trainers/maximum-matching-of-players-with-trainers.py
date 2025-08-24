"""
Solution 1: Two Pointers Parallel pointers

player_p
trainer_p

loop invariants:

every player in the left of player_p was already matched with a trainer
every trainer in the left of trainer_p was already matched with a player of it can't be matched

exit condition: if trainer_p == len(trainers) that means that all possible trainers were processed, or if player_p == len(player) that means that all players were matched

player_p = 0
trainer_p = 0


if cur_trainer >= cur_player: increment the count and move both pointers
else: move trainer poitner


t: O(N log n+ M log M)
s: O(1)


"""


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort() 

        matches = p1 = t1 = 0 
        
        while p1 < len(players) and t1 < len(trainers):
            if trainers[t1] >= players[p1]:
                matches += 1
                p1 += 1
            t1 += 1

        return matches

