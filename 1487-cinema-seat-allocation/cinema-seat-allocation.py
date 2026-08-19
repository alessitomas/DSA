"""
option 1: 2,3,4,5
option 2: 4,5,6,7
option 3: 6,7,8,9


all false

done ^

option 1: true 
option 2: true
option 3: true

done ^

-> 2 

option 1: false 
option 2: true
option 3: true

or 

option 1: true 
option 2: true
option 3: false

-> 1

option 1: true 
option 2: false
option 3: true

-> 2


row_eval = 1
count = 1


row_eval = 2
count = 2


row_eval = 3
count = 4

count = (n - row_eval) * 2


1 
2
3

n = 3

2
"""


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reservedSeats.sort()
        set1 = set([2, 3, 4, 5])
        set2 = set([4, 5, 6, 7])
        set3 = set([6, 7, 8, 9])
        option1 = option2 = option3 = True
        
        cur_row = None
        row_count = 0
        total = 0
        
        for i, reserved in enumerate(reservedSeats):
            r, c = reserved

            if cur_row is None:
                cur_row = r
            
            # next row, process prev row
            if r != cur_row:
                row_count += 1 
                if not (option1 or option2 or option3):
                    total += 0
                elif option1 and option3:
                    total += 2
                else: 
                    total += 1
                
                option1 = option2 = option3 = True
                cur_row = r
           

            if c in set1:
                option1 = False
            if c in set2:
                option2 = False
            if c in set3:
                option3 = False

        row_count += 1 
        if not (option1 or option2 or option3):
            total += 0
        elif option1 and option3:
            total += 2
        else: 
            total += 1

        return total + (n - row_count) * 2
                
        
        