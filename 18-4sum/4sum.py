class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        lookup = set()
        output = []
        nums.sort()

        for a in range(len(nums) - 3):
            for b in range(a + 1, len(nums) - 2):
                first = nums[a]
                second = nums[b]

                c = b + 1
                d = len(nums) - 1

                while (c < d):
                    sum = first + second + nums[c] + nums[d]
                    quad = (first, second, nums[c], nums[d])

                    if (sum == target):
                        if (quad not in lookup):
                            output.append([first, second, nums[c], nums[d]])
                        lookup.add(quad)
                        c += 1
                        d -= 1
                    elif (sum < target):
                        c += 1
                    else:
                        d -= 1

        return output


        return result
        