var shipWithinDays = function(weights, days) {
    let i = Math.max(...weights)
    let j = weights.reduce((a, b)=> a + b, 0)
    let min_weight = Infinity

    function canShip(capacity) {
        let currWeight = 0
        let no_of_days = 1

        for (let weight of weights) {
            currWeight += weight
            if (currWeight > capacity) {
                currWeight = weight
                no_of_days += 1
            }
        }
        return no_of_days <= days
    }    

    while (i <= j) {
        let capacity = Math.floor((i + j) / 2)
        if (canShip(capacity)) j = capacity - 1  
        else i = capacity + 1
    }


    return i
};