"""

[[2, 1, 5], [2,5,6]], 2 -> true

"""

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        capacity_at_position = [0] * 1000
        # touching bounds for interval
        
        for passengers, pickup, dropoff in trips:
            for i in range(pickup, dropoff):
                capacity_at_position[i] += passengers

        
        return all (
            c <= capacity
            for c in capacity_at_position
        )
        


        