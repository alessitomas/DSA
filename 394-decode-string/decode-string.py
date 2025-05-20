class Solution:
    #  s = "2[abc]3[cd]ef"
    # decodeString("2[abc]3[cd]ef")
    # dfs_decoder("2[2[abc]]3[cd]ef") =  2 * dfs_decoder([2[abc]]) + 3 * dfs_decoder(cd) + ef
    # 
    def decodeString(self, s: str) -> str:
        def get_multiplayer(initial_index):
            num_string = []
            # get num
            while s[initial_index].isdigit():
                num_string.append(s[initial_index])
                initial_index += 1
            
            return int("".join(num_string)), initial_index
            
        # return the moved position of initial_index
        # return the extracted segment
        def extract_expression(initial_index):
            # get expression
            open_brackets = 1
            start_index = initial_index
            while open_brackets > 0:
                if s[initial_index] == "[":
                    open_brackets += 1
                if s[initial_index] == "]":
                    open_brackets -= 1
                initial_index += 1
        
            return initial_index - 2
        # []
        # 2[2[abc]]3[cd]ef
        # 2[abc]
         # s[initial_index] = "["
         # a
         # c
        def dfs_decoder(initial_index, final_index):
            decoded_string = []
            
            # looping every char
            while initial_index <= final_index:
                # if it is alphabeth out of expression
                if s[initial_index].isalpha():
                    decoded_string.append(s[initial_index])
                    initial_index += 1
                # needs to be a number to start expression
                else:
                    # index at frist brackets
                    # num = 2
                    # s[initial_index] = "["
                    num, initial_index = get_multiplayer(initial_index)
                    # s[expression_start] = "2"
                    # s[expression_end] = "]"
                    expression_end = extract_expression(initial_index+1)
                    decoded_expression = dfs_decoder(initial_index+1, expression_end)
                    initial_index = expression_end + 2
                    for i in range(num):
                        for char in decoded_expression:
                            decoded_string.append(char)
            
            return decoded_string 
        
        return "".join(dfs_decoder(0, len(s) -1))
                    
                
            
        