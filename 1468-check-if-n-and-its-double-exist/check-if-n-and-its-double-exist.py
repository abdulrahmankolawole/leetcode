class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        lookup = Counter(arr)

        for num in arr:
            if (num != 0 and (num * 2) in lookup):
                return True
            if (num == 0 and lookup[num] > 1):
                return True
        return False

        