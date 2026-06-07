class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute factorials for binomial coefficients
        max_val = m
        fact = [1] * (max_val + 1)
        inv_fact = [1] * (max_val + 1)
        for i in range(1, max_val + 1):
            fact[i] = fact[i - 1] * i % MOD
        
        inv_fact[max_val] = pow(fact[max_val], MOD - 2, MOD)
        for i in range(max_val - 1, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        def nCr(n, r):
            if r > n or r < 0:
                return 0
            return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD
        
        pow_cache = [[1] * (m + 1) for _ in range(n)]
        for i in range(n):
            for c in range(1, m + 1):
                pow_cache[i][c] = pow_cache[i][c - 1] * nums[i] % MOD
        
        max_pos = n + 30  # enough to handle carry bits beyond nums length
        
        @lru_cache(None)
        def dp(pos: int, carry: int, set_bits: int, chosen: int) -> int:
            if pos == max_pos:
                return 1 if carry == 0 and set_bits == k and chosen == m else 0
            
            res = 0
            if pos < n:
                max_count = m - chosen
                for count in range(max_count + 1):
                    bit = (count + carry) & 1
                    new_carry = (count + carry) >> 1
                    new_set_bits = set_bits + bit
                    if new_set_bits > k or chosen + count > m:
                        continue
                    ways = nCr(m - chosen, count)
                    sub_res = dp(pos + 1, new_carry, new_set_bits, chosen + count)
                    if sub_res:
                        res += sub_res * pow_cache[pos][count] % MOD * ways
                        res %= MOD
            else:
                # only carry bits remain
                bit = carry & 1
                new_carry = carry >> 1
                new_set_bits = set_bits + bit
                if new_set_bits <= k:
                    res = dp(pos + 1, new_carry, new_set_bits, chosen)
            return res % MOD
        
        return dp(0, 0, 0, 0)
