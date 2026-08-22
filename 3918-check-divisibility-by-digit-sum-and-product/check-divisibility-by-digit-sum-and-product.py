class Solution:
    def checkDivisibility(self, n: int) -> bool:
        total_sum = 0
        total_product = 1
        n_copy = n
        
        # loop through digits
        while n_copy > 0:
            least_significant_digit = n_copy % 10
            total_sum += least_significant_digit
            total_product *= least_significant_digit
            n_copy = n_copy // 10

        return n % (total_sum + total_product) == 0


        