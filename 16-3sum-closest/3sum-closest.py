class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        summ = 0
        min_diff = float("inf")

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while (left < right):
                curr_sum = nums[i] + nums[left] + nums[right]

                if (curr_sum == target):
                    return curr_sum
                diff = abs(curr_sum - target)
                if (diff < min_diff):
                    summ = curr_sum
                    min_diff = diff
                if (curr_sum < target):
                    left += 1
                else:
                    right -= 1


        return summ