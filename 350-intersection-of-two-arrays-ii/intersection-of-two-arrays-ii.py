class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lookup = {}
        output = []

        for num in nums1:
            if (not num in lookup):
                lookup[num] = 0
            lookup[num] += 1

        for num in nums2:
            if (num in lookup and lookup[num]):
                output.append(num)
                lookup[num] -= 1
        
        return output
        