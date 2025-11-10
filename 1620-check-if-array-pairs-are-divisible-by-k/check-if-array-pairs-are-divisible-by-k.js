var canArrange = function(arr, k) {
    let lookup = {}

    for (let num of arr) {
        rem = ((num % k) + k) % k
        if (!(rem in lookup)) lookup[rem] = 0
        lookup[rem] += 1
    }    

    if (0 in lookup) {
        if (lookup[0] % 2 !== 0) return false
    }

    for (let i = 1; i < k; i++) {
        if (lookup[(i + k) % k] != lookup[(k - i + k) % k]) return false
    }

    return true
};