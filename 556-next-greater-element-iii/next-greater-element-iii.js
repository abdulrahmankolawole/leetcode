var nextGreaterElement = function(n) {
    let array = n.toString().split("")
    let breakIndex = -1

    for (let i = array.length - 2; i >= 0; i--) {
        if (array[i] < array[i + 1]) {
            breakIndex = i
            break
        }
    }    

    if (breakIndex == -1) return breakIndex

    let swapIndex = -1

    for (let i = array.length - 1; i > breakIndex; i--) {
        if (array[i] > array[breakIndex]) {
            swapIndex = i
            break
        }
    }

    [array[swapIndex], array[breakIndex]] = [array[breakIndex], array[swapIndex]]
    i = breakIndex + 1
    j = array.length - 1

    while (i < j) {
        [array[i], array[j]] = [array[j], array[i]]
        i += 1
        j -= 1
    }

    let result = Number(array.join('')) 

    return result > Math.pow(2, 31) -1 ? - 1 : result


};