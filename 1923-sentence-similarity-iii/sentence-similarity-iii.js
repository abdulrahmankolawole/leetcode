var areSentencesSimilar = function(sentence1, sentence2) {
    let arr1 = sentence1.split(" ")
    let arr2 = sentence2.split(" ")

    if (arr1.length > arr2.length) {
        [arr1, arr2] = [arr2, arr1]
    }

    let i = 0
    let j = arr1.length
    let k = arr2.length

    while (i < arr1.length && arr1[i] == arr2[i]) {
        i += 1
    }

    while (j >= 0 && k >= 0 && arr1[j] == arr2[k]) {
        j -= 1
        k -= 1
    }

    return i > j

};