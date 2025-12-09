var reverseWords = function(s) {
    let split = s.trim().split(" ")
    let array = []

    for (let word of split) {
        if (word) array.push(word)
    }
    let i = 0
    let j = array.length - 1

    while (i < j) {
        [array[i], array[j]] = [array[j], array[i]]
        i += 1
        j -= 1
    }   

    return array.join(" ")


};