class Solution:
    def countPrimes(self, n: int) -> int:
        n = max(n, 2)

        is_prime = [True] * n
        is_prime[0] = False
        is_prime[1] = False

        for current_num in range(2, ceil(sqrt(n))):
            if is_prime[current_num]:
                for composite in range(current_num**2, n, current_num):
                    is_prime[composite] = False

        prime_count = is_prime.count(True)
        
        return prime_count
