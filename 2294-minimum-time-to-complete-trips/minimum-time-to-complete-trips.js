var minimumTime = function(time, totalTrips) {
    let i = 1
    let j = (Math.max(...time) * totalTrips)
    time.sort((a, b)=> a - b)

    function canTrip(time_taken) {
        let trips = 0
        for (let t of time) {
            trips += Math.floor(time_taken / t)
        }
        return trips >= totalTrips
    }

    while (i <= j) {
        let mid = Math.floor((i + j) / 2)
        if (canTrip(mid)) {
            j = mid - 1
        }
        else i = mid + 1
    }    
    return i
};