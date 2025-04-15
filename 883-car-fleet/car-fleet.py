class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        index_pos_sorted = sorted(enumerate(position), key = lambda x : x[1])
        print("index_pos_sorted", index_pos_sorted)
        sorted_speed = []
        for index, _ in index_pos_sorted:
            sorted_speed.append(speed[index])
        
        print("sorted_speed.append", sorted_speed)
        # position
        # speed

        time = []
        for i in range(len(index_pos_sorted)):
            time.append((target - index_pos_sorted[i][1]) / sorted_speed[i])
        print("time", time)
        fleet_count = 1

        for i in range(len(time) -1, 0, -1):
            if time[i-1] <= time[i]:
                time[i-1] = time[i]
            else:
                fleet_count += 1
        
        return fleet_count
   
