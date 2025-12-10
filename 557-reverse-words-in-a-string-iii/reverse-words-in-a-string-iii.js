var reverseWords = function(s) {

    function reverseWord(word) {
        let array = word.split("")
        let i = 0
        let j = array.length - 1

        while (i < j) {
            [array[i], array[j]] = [array[j], array[i]]
            i += 1
            j -= 1
        }

        return array.join("")
    }
    let array = s.split(" ")
    let i = 0
    let j = array.length - 1
    
    for (let i = 0; i < array.length; i++) {
        array[i] = reverseWord(array[i])
    }

    return array.join(" ")
};