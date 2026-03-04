var dividePlayers = function(skill) {
    let total = skill.reduce((a, b)=> a + b, 0)
    if (2 * total % skill.length != 0) return -1
    let lookup = {}
    let target = Math.floor((2 * total) / skill.length )
    let output = 0

    for (let num of skill) {
        if (!(num in lookup)) lookup[num] = 0
        lookup[num] += 1
    }
    
    for (let num of skill) {
        if (!(lookup[num])) continue
        let diff = target - num
        if (!(lookup[diff])) return -1
        if (diff in lookup) {
            output += (num * diff)
            lookup[diff] -= 1
            lookup[num] -= 1
        }
    }

    return output
};