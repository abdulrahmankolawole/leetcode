class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        i = 0
        j = max(arr)
        min_diff = float("inf")
        result = float("inf")

        def addSum(num):
            total = 0
            
            for val in arr:
                total += num if val > num else val

            return total

        while (i <= j):
            mid = (i + j) // 2

            summ = addSum(mid)

            if (summ == target):
                return mid
            if (summ < target):
                i = mid + 1
            else:
                j = mid - 1

            diff = abs(summ - target)

            if (diff < min_diff or (diff == min_diff and mid < result)):
                result = mid
                min_diff = diff

        
        return result
        