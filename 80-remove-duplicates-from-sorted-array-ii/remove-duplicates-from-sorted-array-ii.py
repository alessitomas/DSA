class Solution:
    # [1,1,2,2,3,4,5,5]
    # []
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # start overmapped
        # end exclusive
        def shift_left(start, arr):

            for i in range(start, len(arr) -1 ):
                arr[i] = arr[i+1]



        cur_app = 1
        removals = 0
        idx = 1


        while idx < len(nums) - removals:
            if nums[idx] != nums[idx-1]:
                idx += 1
                cur_app = 1
            else:
                if cur_app == 1:
                    cur_app += 1
                    idx += 1
                else:
                    shift_left(idx, nums)
                    removals += 1
                    cur_app = 2

        return len(nums) - removals





        