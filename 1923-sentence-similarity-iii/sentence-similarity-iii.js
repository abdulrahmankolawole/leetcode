var areSentencesSimilar = function(sentence1, sentence2) {
    let arr1 = sentence1.split(" ")
    let arr2 = sentence2.split(" ")    

    if (arr2.length < arr1.length) {
        [arr1, arr2] = [arr2, arr1]
    }

    i = 0
    j = arr1.length - 1
    r = arr2.length - 1

   
    while (i < arr1.length && arr1[i] == arr2[i]) i += 1

    while (j >= 0 && r >= 0 && arr1[j] == arr2[r]) {
        j -= 1
        r -= 1
    }

    return i > j
};