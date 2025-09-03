class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        i = 1
        j = max(time) * totalTrips

        def canTrip(mid):
            completed_trips = 0
            for t in time:
                completed_trips += (mid // t)

            return completed_trips >= totalTrips
                
        while (i <= j):
            mid = (i + j) // 2

            if (canTrip(mid)):
                j = mid - 1
            else:
                i = mid + 1

        return i

        