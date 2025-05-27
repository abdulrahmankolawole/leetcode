var isLongPressedName = function(name, typed) {
    let i = 0
    let j = 0
    if (typed.length < name.length) return false

    while (j < typed.length) {
        if (i < name.length && name[i] == typed[j]) {
            i += 1
        }
        else if (j == 0 || typed[j] != typed[j - 1]) return false
        j += 1
    }
    
    return i == name.length    
};