var numRescueBoats = function(people, limit) {
    weights = [...people].sort((a, b)=> a - b)

    let boats = 0

    i = 0
    j = people.length - 1

    while (i <= j) {
        boats += 1

        if (weights[i] <= limit - weights[j]) {
            i += 1
        }
        j -= 1
    }    

    return boats
};