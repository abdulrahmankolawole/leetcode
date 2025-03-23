var minimumCardPickup = function(cards) {
    let lookup = {}
    let i = 0
    let j = 0
    let minSize = Infinity

    while (j < cards.length) {

        let curr = cards[j]
        
        if (curr in lookup) {
            minSize = Math.min(minSize, j - lookup[curr] + 1)
            i += 1
        }

        lookup[curr] = j
        j += 1
    }    

    return minSize == Infinity ? - 1 : minSize
};