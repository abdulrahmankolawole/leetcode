var minimumCardPickup = function(cards) {
    let lookup = new Set()
    let output = Infinity
    let j = 0

    while (j < cards.length) {
        let card = cards[j]

        if (card in lookup) {
            let size = j - lookup[card] + 1
            output = Math.min(output, size)
        }
        
        lookup[card] = j 
        j ++ 
    }    

    return output == Infinity? -1 : output
};