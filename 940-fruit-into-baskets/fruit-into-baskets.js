var totalFruit = function(fruits) {
    let i = 0
    let j = 0
    let lookup = {}
    let output = 0

    while (j < fruits.length) {
        fruit = fruits[j]
        if (!(fruit in lookup)) lookup[fruit] = 0
        lookup[fruit] += 1

        while (Object.keys(lookup).length > 2) {
            if (lookup[fruits[i]] == 1) {
                delete lookup[fruits[i]]
            }
            else lookup[fruits[i]] -= 1
            i += 1
        }

        output = Math.max(output, j - i + 1)
        j += 1
    }    

    return output
};