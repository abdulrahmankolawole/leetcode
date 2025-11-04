class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        ending = float("-inf")
        arrows = 0

        if (len(points) == 1):
            return 1

        for point in points:
        # if the current interval is nonoverlapping, increment the count of arrows needed to burst balloons
            if (point[0] > ending):
                arrows += 1
                ending = point[1]

        return arrows
        