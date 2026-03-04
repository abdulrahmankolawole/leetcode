class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1] * len(nums1)
        lookup = {}
        stack = []

        for idx, val in enumerate(nums1):
            lookup[val] = idx

        j = len(nums2) - 1

        while (j >= 0):
            if (not stack):
                stack.append(nums2[j])
            else:
                while (stack and nums2[j] >= stack[-1]):
                    stack.pop()
                if (stack and nums2[j] in lookup):
                    idx = lookup[nums2[j]]
                    result[idx] = stack[-1]
                stack.append(nums2[j])

            j -= 1

        return result

        