class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        index_pos_sorted = sorted(enumerate(position), key = lambda x : x[1])
    
        sorted_speed = []
        for index, _ in index_pos_sorted:
            sorted_speed.append(speed[index])
        
    
        # position
        # speed

        time = []
        for i in range(len(index_pos_sorted)):
            time.append((target - index_pos_sorted[i][1]) / sorted_speed[i])
        
        fleet_count = 1

        for i in range(len(time) -1, 0, -1):
            if time[i-1] > time[i]:
                fleet_count += 1
            else:
                time[i-1] = time[i]
        
        return fleet_count
   
