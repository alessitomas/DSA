"""
N functions.

len(logs) = 2 N




id:0 end: 6
id:0 start:0

# call stack



completed_task_total_time = 4

id 1: took (end, 5) - (start, 2) + 1 = 4

id 0: tool (end, 6) - (start, 0) + 1 - completed_task_total_time = 3

# end - start + 1 because start is inclusive




    |----------||--------------||----------||----------|

"0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"



current log is start and top of stack is start

I know exactly the time that top start segemnt took, I can store it.


current end and top of stack is a start, I know exaclty how much time that function call took.

I can pop the hole function call.

Current end and stack is empty, I need to have store the last record time to add its segment time to the respective function call.

stack store only starts

current:

start
    stack is empty just add it
    else: pop it and store its segment, then current start add it

end 
    stack is not empty, calculate hole function exec time
    stack is empty calculate its segemnt time

"""
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        call_stack = []
        times = [0] * n
        
        
        for l in logs:
            cur_id, cur_event, cur_timestamp = l.split(":")
            cur_timestamp, cur_id = int(cur_timestamp), int(cur_id)
            
            if cur_event == "start":
                call_stack.append((cur_id, cur_timestamp))
            else:
                _ , last_timestamp = call_stack.pop(-1)
                
                # inclusive start and end
                times[cur_id] += (cur_timestamp - last_timestamp) + 1
                
                if call_stack:
                    open_id, _ = call_stack[-1]
                    times[open_id] -= (cur_timestamp - last_timestamp) + 1
        
        return times

""" 
                                                           i
["0:start:0","0:start:2","0:end:5","1:start:7","1:end:7","0:end:8"]


 0 0 0 0 0 0 
[0,1,2,3,4,5,6,7,8]

[2, ]


last = 7

[7, 1]

id0: + 2 - 0 
id0: (5 - 2) + 1
id1: 7 - 7 + 1
id0: 8 - 7

[0,1,2,3,4,5]


""" 