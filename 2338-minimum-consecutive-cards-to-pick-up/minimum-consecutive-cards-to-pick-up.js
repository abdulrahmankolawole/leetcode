var minimumCardPickup = function(cards) {
    let output = Infinity
    let lookup = {}
    let j = 0

    while (j < cards.length) {
        let card = cards[j]

        if (card in lookup) {
            output = Math.min(output, j - lookup[card] + 1)
        }
        lookup[card] = j
        j += 1
    }  
    return output == Infinity? - 1: output
};