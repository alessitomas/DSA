"""
Solution 1:

reverse function

traverse the input with two pointer

one will stay at the first char of a word and the other will find the first space.

Then is possible to calulatt the range of indices of the words character and use them as arguments for the word reversal.

Optimal 
T: O(N), since I will iterate less then 2 times for each character
S: O(N)


start = index of the first char of a given char
end = index of the last char of that word

while end < len(s)
"""


"""

start = 3

0123456 
Mr Ding
      i

reverse [0-1]

rM Ding

reverse [3-6]
rM Ding

"""


# class Solution:
#     def reverseWords(self, s: str) -> str:
#         def reverse(start, end, arr):
#             while end > start:
#                 arr[start], arr[end] = arr[end], arr[start]
#                 start += 1
#                 end -= 1
        
#         if not s:
#             return s 
        
#         chars = list(s)
#         start = None

#         for i in range(len(chars)):
            
#             if chars[i] != " " and start is None:
#                 start = i
                
#             if chars[i] != " " and i == len(chars) - 1:
#                 reverse(start, i, chars)

#             if start is not None and chars[i] == " ":
#                 reverse(start, i - 1, chars)
#                 start = None
                
#         return "".join(chars)
        
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         def reverse(arr):
#             start, end = 0, len(arr) -1
#             while end > start:
#                 arr[start], arr[end] =  arr[end], arr[start] 
#                 start += 1
#                 end -= 1

#         words = s.split()
#         words_lists = [list(w) for w in words]

#         for i, w_list in enumerate(words_lists):
#             reverse(w_list)
#             words_lists[i] = "".join(w_list)
        

#         return " ".join(words_lists) 


            

class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(start, end, arr):
            while end > start:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        
        if not s:
            return s 
        
        chars = list(s)
        start = end = 0

        while end < len(chars):
            if chars[start] == " ":
                start += 1
                if start > end:
                    end += 1
            
            elif chars[end] != " ":
                end += 1
            
            else:
                reverse(start, end - 1, chars)
                start, end = end + 1, end + 1
        
        if chars[-1] != " ":
            reverse(start, len(chars) - 1, chars)

        return "".join(chars)
