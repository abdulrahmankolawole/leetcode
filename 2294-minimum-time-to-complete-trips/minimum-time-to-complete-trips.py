class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        i = 1
        j = max(time) * totalTrips
        # time.sort()

        def canTrip(mid):
            trips_completed = 0

            for t in time:
                trips_completed += math.floor(mid / t)

            return trips_completed >= totalTrips


        while (i <= j):
            mid = (i + j) // 2

            if (canTrip(mid)):
                j = mid - 1
            else:
                i = mid + 1

        return i
        