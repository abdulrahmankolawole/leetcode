class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarr_sum = []
        output = 0
        modulo = (10 ** 9) + 7

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                subarr = nums[i: j + 1]
                subarr_sum.append(sum(subarr))

        subarr_sum.sort()

        # print(subarr_sum)

        for i in range(left - 1, right):
            output += subarr_sum[i]


        return output % modulo
        