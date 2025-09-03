var successfulPairs = function(spells, potions, success) {
    let output = []
    potions.sort((a, b)=> a - b)

    function binarySearch(spell) {
        let i = 0
        let j = potions.length - 1

        while (i <= j) {
            let mid = Math.floor((i + j) / 2)
            if (potions[mid] * spell >= success) {
                j = mid - 1
            }
            else i = mid + 1
        }
        return i
    }

    for (let i = 0; i < spells.length; i++){
        let spell = spells[i]
        let index = binarySearch(spell)
        output[i] = potions.length - index
    }

    return output
};