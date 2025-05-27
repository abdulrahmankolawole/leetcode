class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        lookup = set()
        
        for i in range(len(nums) - 1):
            first = nums[i]

            a = i + 1
            b = len(nums) - 1

            while (a < b):
                sum = first + nums[a] + nums[b]
                if (sum == 0):
                    triplets = (first, nums[a], nums[b])
                    if (triplets not in lookup):
                        output.append([first, nums[a], nums[b]])
                    lookup.add(triplets)
                    a += 1
                    b -= 1
                elif (sum < 0):
                    a += 1
                else:
                    b -= 1

        return output

        