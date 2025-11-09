class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        lookup = Counter(nums)
        count = 0

        if (k == 0):
            for key, value in lookup.items():
                if (value > 1):
                    count += 1

        else:
            for key, value in lookup.items():
                if (key + k in lookup):
                    count += 1


        return count
        