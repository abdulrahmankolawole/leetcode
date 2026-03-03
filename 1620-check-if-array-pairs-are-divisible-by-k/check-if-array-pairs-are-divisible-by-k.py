class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        lookup = {}

        for num in arr:
            rem = ((num % k) + k) % k

            if (rem not in lookup):
                lookup[rem] = 0
            lookup[rem] += 1

        if (0 in lookup):
            if (lookup[0] % 2 != 0):
                return False
        
        for i in range(1, k):
            if ((i + k) % k not in lookup):
                continue
            if (k-i + k) % k not in lookup:
                return False
            if ((lookup[(i + k) % k] != lookup[(k - i + k) % k])):
                return False

        return True
        