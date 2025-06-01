class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums is None: return []
        if len(nums) < 3: return []        
        # b + c = -a
        # N LOG N
        nums.sort()
        triplets = []
        # i , j
        prev = None
        for i in range(len(nums) - 1):
            j = i + 1
            k = len(nums) - 1
            cur_target = (-1) * (nums[i])
            if nums[i] == prev:
                continue 
            prev = nums[i]
            while k > j:
                cur_sum = nums[k] + nums[j]
                if cur_sum > cur_target:
                    k -= 1
                elif cur_sum < cur_target:
                    j += 1
                else:
                    triplets.append([nums[i],nums[j],nums[k]])
                    j += 1
                    while k > j and nums[j] == nums[j-1]:
                        j += 1
                    
                    k -= 1

        
        return  triplets




                
                
                

                    
                
        
        