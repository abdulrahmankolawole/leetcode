var areSentencesSimilar = function(sentence1, sentence2) {

    let arrOne = sentence1.split(" ")
    let arrTwo = sentence2.split(" ")

    if (arrTwo.length < arrOne.length) {
        [arrOne, arrTwo] = [arrTwo, arrOne]
    }

    let l1 = 0
    let l2 = 0
    let r1 = arrOne.length - 1
    let r2 = arrTwo.length - 1

    while (l1 < arrOne.length && arrOne[l1] == arrTwo[l1]) {
        l1 += 1
    }

    while (r1 >= 0 && r2 >=0 && arrOne[r1] == arrTwo[r2]) {
        r2 -= 1
        r1 -= 1
    }

    return l1 > r1
};