var merge = function(intervals) {
    // sort the intervals by their first numbers
    intervals.sort((a, b)=> a[0] - b[0])

    if (intervals.length === 1) {
        return intervals
    }
    let result = [intervals[0]]

    for (let i = 1; i < intervals.length; i++) {
    // if the 2nd number in the prev interval is greater than or equal to the first number in the current interval, merge them
        let prev = result.at(-1)
        let current = intervals[i]

        if (prev[1] >= current[0]) {
            result[result.length - 1] = [prev[0], Math.max(prev[1], current[1])]
        }
        else{
            result.push(current)
        }
    }

    return result

         
};