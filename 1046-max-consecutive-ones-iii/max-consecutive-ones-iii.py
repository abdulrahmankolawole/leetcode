# use a sliding window approach
# declare two pointers i and j with initial value 0

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        size = 0
        count_of_zeroes = 0
        
        while (j < len(nums)):
            
            if (nums[j] == 0):
                count_of_zeroes += 1
            
            while (count_of_zeroes > k):
                if (nums[i] == 0):
                    count_of_zeroes -=1
                i +=1

            size = max(size, j - i + 1)

            j += 1

        return size



        
        