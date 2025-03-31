class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        my_set = set()
        nums.sort()

        for a in range(len(nums) - 3):
            for b in range(a + 1, len(nums) - 2):

                first = nums[a]
                second = nums[b]

                c = b + 1
                d = len(nums) -1

                while (c < d):
                    total = first + second + nums[c] + nums[d]

                    if (total == target):
                        four = (first, second, nums[c], nums[d])

                        if (four not in my_set):
                            output.append([first, second, nums[c], nums[d]])
                            my_set.add(four)
                        
                        c += 1
                        d -= 1

                    elif (total < target):
                        c += 1

                    else:
                        d -= 1


        return output

        