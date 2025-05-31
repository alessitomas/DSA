class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums is None: return []
        if len(nums) < 3: return []        
        
        triplets = set()
        # N LOG N
        nums.sort()
        
        # N^3
        #  b + c = 0 - 
        # [1,2,3]
        for i in range(len(nums) - 1):
            j = i + 1
            k = len(nums) - 1
            cur_target = (-1) * (nums[i])
            
            while k > j:
                cur_sum = nums[k] + nums[j]
                if cur_sum > cur_target:
                    k -= 1
                elif cur_sum < cur_target:
                    j += 1
                else:
                    triplets.add((nums[i],nums[j],nums[k]))
                    j += 1
                    k -= 1

        
        return [ [i,j,k] for (i,j,k) in triplets]




                
                
                

                    
                
        
        