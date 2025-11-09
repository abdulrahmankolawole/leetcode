var numPairsDivisibleBy60 = function(time) {
    let lookup = {}
    let count = 0

    for (let t of time) {
        let remainder = t % 60

        if (remainder) {
            let diff = 60 - remainder
            if (diff in lookup) count += lookup[diff]
            if (!(remainder in lookup)) lookup[remainder] = 0
            lookup[remainder] += 1
        }
        else {
            if (!(lookup[0])) lookup[0] = 0
            count += lookup[0]
            lookup[0] += 1
        }
    }
    return count
};