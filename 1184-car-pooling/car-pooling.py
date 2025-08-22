"""

Solution 1: 

N, N-1, N-2, N-3 ... 1

N/2 * (N + 1)

T: O(N), where N is the length or trips, because for every trip that is in the worste case 1000 constant iterations
S: O(1), 1000 constant space

or reframed

T: O(N * maxDropOff)
S: O(maxDropOff)

Solution 2:

Keep an array representing each km of the road.
Iterate over the trips arr, and increment passengers for pickup and decrement of dropoff
Iterate over the road arr to verify if it goes out of limit


T: O(N + maxDropOff)
S: O(maxDropOff)


"""

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        capacity_at_position = [0] * 1001
        # touching bounds for interval
        
        for passengers, pickup, dropoff in trips:
            capacity_at_position[pickup] += passengers
            capacity_at_position[dropoff] -= passengers
            

        cur_capacity = 0
        for c in capacity_at_position:
            cur_capacity += c
            if cur_capacity > capacity:
                return False
        
        return True 
        


        