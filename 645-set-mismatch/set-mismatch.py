class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        lookup = Counter(nums)
        result = [0, 0]
        N = len(nums)

        for i in range(1, N + 1):
            if (i not in lookup):
                result[1] = i
            elif (lookup[i] == 2):
                result[0] = i

        return result