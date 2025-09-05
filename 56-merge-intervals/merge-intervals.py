"""


|---|
   |--------|
                |-------------|
                                    |--------------|


how can I know when two intervals overlap?

|---| x
  |--------| y

|---| x
    |--------| y

|---| x
        |--------| y

|---| x
|---| y

|-------| x
|---| y

if x_end >= y_start that means that ther intervals overlap givent that x_start <= y_start

how can I merge overlapping intervals?


[start_x, max(end_x, end_y)]


I can use a stack (aka list) to store the intervals while iterating through the interval arrays.

if the interval selected overlaps with the last registered interval merge them, else append it.


Since the interval array will be sorted, buy (start, end) overlapping intervals will be next to each other.

T: O(N log N) due to sorting
S: O(N) to create the output array

"""





class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []
        
        def overlap(first, second):
            return first[1] >= second[0]

        for inter in intervals:
            if len(merged) > 0 and overlap(merged[-1], inter):
                first = merged[-1]
                merged[-1] = [first[0], max(first[1], inter[1])]
            else:
                merged.append(inter)

        return merged

        