class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(key= lambda x: -x)
        discounts.sort(key= lambda x: -x)
        total = 0
        d_index = 0

        for p in prices:
            cur_price = p
            if d_index < len(discounts):
                cur_price = cur_price * (100 - discounts[d_index])  / 100 
                d_index += 1
            total += cur_price

        return total
                


        
        