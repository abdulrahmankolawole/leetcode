class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        lookup = Counter(nums)

        for num, freq in lookup.items():
            if (freq % 2 != 0):
                return False


        return True
        