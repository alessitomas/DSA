# map string to int  {"1": 1, "2": 2, "3": 3, "4": 4 ...}

# string to int function
# base = 1
# for i in range(str)
#  base * mapped(str)
#  base *= 10

# Time: O(M + N)
# space O(1)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        NUM_MAP = {
            "0": 0, 
            "1": 1, 
            "2": 2, 
            "3": 3, 
            "4": 4, 
            "5": 5, 
            "6": 6, 
            "7": 7, 
            "8": 8, 
            "9": 9
        }
        
        def string_to_int(str_num):
            base = 1
            num = 0
            for i in reversed(range(len(str_num))):
                char = str_num[i]
                num += NUM_MAP[char] * base
                base *= 10
            return num
        
        return str(string_to_int(num1) * string_to_int(num2))

        