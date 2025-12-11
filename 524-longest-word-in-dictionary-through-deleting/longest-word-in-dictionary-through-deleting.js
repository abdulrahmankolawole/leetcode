// var findLongestWord = function(s, dictionary) {
    
//     var isSubsequence = function(s, t) {
//         let i = 0
//         let j = 0

//         while (j < t.length) {
//             if (s[i] == t[j]) i += 1
//             j += 1
//         }   

//         return i == s.length
//     };

//     let output = ""
//     let maxLength = 0

//     for (let word of dictionary) {
//         if (isSubSeq(s, word)) {
//             if (word.length > output.length) {
//                 output = word
//             }
//             else if (word.length == output.length) {
//                 output = output < word ? output : word
//             }
//         }
//     }
//     return output
// };

var findLongestWord = function(s, dictionary) {

    dictionary.sort((a, b)=> b.length == a.length ? a.toLowerCase().localeCompare(b.toLowerCase()) : b.length - a.length)
    console.log(dictionary)
    
    function isSubseq(s, t) {
        let i = 0
        let j = 0

        while (j < t.length) {
            if (s[i] == t[j]) i += 1
            j += 1
        }   

        return i == s.length
    };

    let output = ""
    let maxLength = 0

    for (let word of dictionary) {
        if (isSubseq(word, s)) return word
    }
    return output
};