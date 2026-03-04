class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        lookup = Counter(nums)

        nums.sort(key = lambda x: (lookup[x], -x))
        return nums
        