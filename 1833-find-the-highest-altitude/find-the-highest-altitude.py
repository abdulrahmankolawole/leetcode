class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        output = 0
        sum = 0

        for num in gain:
            sum += num
            output = max(sum, output)

        return output
        