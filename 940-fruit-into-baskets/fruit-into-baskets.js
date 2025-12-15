var totalFruit = function(fruits) {
    let i = 0
    let j = 0
    let lookup = new Map()
    let output = 0

    while (j < fruits.length) {
        let fruit = fruits[j]

        lookup.set(fruit, lookup.get(fruit) + 1 || 1)

        while (lookup.size > 2) {
            fruitCount = lookup.get(fruits[i])
            if (fruitCount == 1) lookup.delete(fruits[i])
            else lookup.set(fruits[i], fruitCount - 1)
            i += 1
        }

        output = Math.max(output, j - i + 1)
        j += 1
    }

    return output
};