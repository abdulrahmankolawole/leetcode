class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:

        subarray_sums = []
        modulo = (10 ** 9) + 7
        
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                subarray = nums[i: j + 1]
                summ = sum(subarray)
                subarray_sums.append(summ)

        subarray_sums.sort()
        output = 0
        for i in range(left - 1, right):
            output += subarray_sums[i] 

        return output % modulo
        