"""

anagram -> permutation of chars

Solution 1:

map: (sorted string) : group []


for every word in strs
    sort the word
    if sorted word is in map add it to the group, else create a new group

create a list out of the groups

T: O(N L (log L) , where N is the length of the array and L is the largest string in the arr
S: O(N * L)

10 min


Solution 2:

map: tuple of bit max : group []

for every word in strs
    calculate tuple bit mask

"""


from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anam_2_group = defaultdict(list)
        
        for w in strs:
            sorted_w = "".join(sorted(w))
            anam_2_group[sorted_w].append(w)
            
        return list(anam_2_group.values())
            
           
        