class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        char_list = list(s)
        stack = []
        sequence_count = []
        
        for c in char_list:
            
            if len(stack) > 0 and stack[-1] == c and sequence_count[-1] == k - 1:
                for _ in range(k - 1):
                    stack.pop()
                    sequence_count.pop()

                continue

                        
            if len(stack) == 0 or c != stack[-1]:
                count = 1
            else: 
                count = sequence_count[-1] + 1

            stack.append(c)
            sequence_count.append(count)
            

        return "".join(stack)