var checkIfExist = function(arr) {
    let lookup = {}

    for (let num of arr) {
        if (!(num in lookup)) lookup[num] = 0
        lookup[num] ++ 
    }

    for (let num of arr) {
        if (num === 0 && lookup[num] > 1 )  {
            return true
        } 
        if (num != 0 && (num * 2) in lookup) {
            return true
        } 
    }    
    return false
};