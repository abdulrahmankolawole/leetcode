class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lookup = Counter(nums1)
        output = []

        for num in nums2:
            if num in lookup:
                if (lookup[num] > 0):
                    output.append(num)
                    lookup[num] -= 1

        return output
        