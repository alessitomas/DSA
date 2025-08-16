"""

Binary Search (log N)

T: O(log N)
S: O(1)



[-2, 4, 7, 8, 8, 8, 8, 10]



output: [4, 6]

I could use binary search to find the transition point in the arr.

To find the first appearence transition point can be formulated as:

for the first appereance:

if arr[m] >= X:
    rp = mid
else:
    lp = mid


        lp               rp
less than X | bigger or equal to X

then rp would be the first appearance, if there is any in the arr.

and for the last appeareance I could do the following transition point:


        lp               rp
less or equal to X | bigger than X


if arr[mid] <= x:
    lp = mid
else: 
    rp = mid


than lp would be the last if there is any in the arr


edge cases, to be handeled before:

- X is not in the array if arr[0] > X or arr[-1] < X.
- if arr[0] is X, than first app is 0.
- if arr[-1] is X, than last app is len(arr) -1.



FP:

length = 8


           rp
  0. 1. 2. 3. 4  5  6.  7
[-2, 4, 7, 8, 8, 8, 8, 10]
        lp
                        
                        
if arr[m] >= X:
    rp = mid
else:
    lp = mid

                   
[3]


"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        def bin_search(is_before, arr, target):
            
            if not arr or arr[0] > target or arr[-1] < target:
                return -1, -1
            
            lp, rp = 0, len(arr) - 1
            
            while rp - lp > 1:
                mid = (lp + rp) // 2
                if is_before(arr[mid], target):
                    lp = mid
                else:
                    rp = mid
                    
            return lp, rp
        
        def find_first(arr, target):
            def is_before_first_app(v , target):
                return v < target
            
            lp, rp = bin_search(is_before_first_app, arr, target)
            
            if lp == -1 or rp == -1:
                return -1
            
            if arr[lp] == target:
                return lp
            
            if arr[rp] == target:
                return rp
            
 
            
            return -1 
            
            
            
            
        def find_last(arr, target):
            def is_before_last_app(v , target):
                return v <= target
            
            lp, rp = bin_search(is_before_last_app, arr, target)
            
            if lp == -1 or rp == -1:
                return -1
            
            if arr[rp] == target:
                return rp
            
            if arr[lp] == target:
                return lp
            
            
            return -1
                
            

        return [find_first(nums, target), find_last(nums, target)]
            
        
        
        
        
        
            
        
        
        
        