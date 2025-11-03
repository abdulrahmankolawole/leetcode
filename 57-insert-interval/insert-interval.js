var insert = function(intervals, newInterval) {
    // if the new interval comes before the current interval, add new interval and the rest of the intervals to the result
    // if the current interval is not overlapping with the new interval, add it to the result
    // else merge the two intervals
    // push the merged interval to the result
    // intervals.sort((a, b)=> a[0] - b[0])
    result = []
    
    for (let i = 0; i < intervals.length; i++) {
        let currentInterval = intervals[i]
        if (newInterval[1] < currentInterval[0]) {
            result.push(newInterval)
            return result.concat(intervals.slice(i))
        }
        else if (currentInterval[1] < newInterval[0]) result.push(currentInterval)
        else {
            newInterval = [Math.min(currentInterval[0], newInterval[0]), Math.max(currentInterval[1], newInterval[1])]
        }
    }
    result.push(newInterval)
    return result

};