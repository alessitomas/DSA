"""
up, down left right pass in the middle or main diagonal
rest can't pass in the middle


  # # #
#
#
#


backtracking enumeration (cur_pos, cur_sequence)


                            NONE
    (0,0), (0,1) ... (3,3) 


C (9,1) + C (9,2) + C(9,3) + C(9,4) ... C(9,9) 

higher bound (9^n)


00      03

30.     33
"""


class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        count = 0

        def is_valid_pos(cur_pos, pos, cur_sequence):
            src_r, src_c = cur_pos 
            dst_r, dst_c = pos

            if pos in cur_sequence:
                return False

            if src_r == dst_r and src_c == dst_c:
                return False

            if src_r == dst_r and abs(src_c - dst_c) > 1:
                return (src_r,1) in cur_sequence
            
            if src_c == dst_c and abs(src_r - dst_r) > 1:
                return (1,src_c) in cur_sequence

            r_delta, c_delta = abs(src_r - dst_r), abs(src_c - dst_c) 

            if r_delta == c_delta and c_delta == 2:
                return (1,1) in cur_sequence

            return True
            

        def backtracking(cur_pos, cur_sequence):
            
            nonlocal count 
            if len(cur_sequence) >= m:
                count += 1
            
            # base case
            if len(cur_sequence) == n:
                return 

            for pos in [(i,j) for i in range(3) for j in range(3)]:
                if not is_valid_pos(cur_pos, pos, cur_sequence):
                    continue 
            
                cur_sequence.add(pos)
                backtracking(pos, cur_sequence)
                cur_sequence.remove(pos)
            
        
        for i in range(3):
            for j in range(3):
                backtracking((i,j), set([(i,j)]))
        
        return count 

        