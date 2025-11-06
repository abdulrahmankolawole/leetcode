class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1] * len(nums1)
        lookup = {}
        stack = []

        for idx, val in enumerate(nums1):
            lookup[val] = idx

        for i in range(len(nums2) -1, -1, -1):
            if (not stack):
                stack.append(nums2[i])
            else:
                while (stack and nums2[i] >= stack[-1]):
                    stack.pop()
                if (stack and nums2[i] in lookup):
                    idx = lookup[nums2[i]]
                    result[idx] = stack[-1]
                stack.append(nums2[i])


        return result

        