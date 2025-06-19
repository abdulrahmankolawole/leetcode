var successfulPairs = function(spells, potions, success) {
    potions.sort((a, b) => a - b)
    let size = spells.length
    let output = new Array(size)

    function bs(spell) {
        let i = 0
        let j = potions.length - 1

        while (i <= j) {
            let mid = Math.floor((i + j)/ 2)
            if (potions[mid] * spell >= success) j = mid - 1
            else i = mid + 1
        }
        return potions.length - i
    }

    for (let i = 0; i < spells.length; i++) {
        output[i] = bs(spells[i])
    }
    return output

};