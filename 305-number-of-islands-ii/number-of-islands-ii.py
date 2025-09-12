"""

union find


keep a set of turned lands.

    for every land increment the connected component count

    do unions with every neighbor of lands that is present on the set
    if a union is made with a land of a different component decrement the total islands


    T: positions * a(positions)
    s: positions

"""



class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        class Node:
            def __init__(self):
                self.par = self
                self.rank = 1

        cc = 0
        def _find(node):
            # find root
            root = node
            
            while root != root.par:
                root = root.par
            
            # path compression

            while node != root:
                nxt_par = node.par
                node.par = root
                node = nxt_par

            return root

        def _union(node_a, node_b):
            nonlocal cc 
            par_a, par_b = _find(node_a), _find(node_b)
            
            if par_a == par_b:
                return
            
            cc -= 1
            if par_a.rank > par_b.rank:
                par_b.par = par_a
            else:
                par_a.par = par_b
                if par_a.rank == par_b.rank:
                    par_b.rank += 1


        
        lands = {}
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        
        land_count = []
        
        for r, c in positions:
            if (r, c) not in lands:
                cc += 1
                node = Node()
                lands[(r,c)] = node
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (nr, nc) in lands:
                        _union(node, lands[(nr,nc)])
                
            land_count.append(cc)

        return land_count



# find not returning root
        