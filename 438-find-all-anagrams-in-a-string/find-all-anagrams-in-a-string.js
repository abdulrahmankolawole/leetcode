var findAnagrams = function(s, p) {
    let output = []
    let obj1 = {}
    let obj2 = {}
    const _ = require("lodash")

    for (let i = 0; i < p.length; i++) {
        obj1[p[i]] = (obj1[p[i]] || 0) + 1
    }   

    for (let i = 0; i < p.length; i++) {
        obj2[s[i]] = (obj2[s[i]] || 0) + 1
    }   

    if (_.isEqual(obj1, obj2)) output.push(0)

    let i = 0
    let j = p.length

    while (j < s.length) {
        obj2[s[j]] = (obj2[s[j]] || 0) + 1

        if (obj2[s[i]] == 1) delete obj2[s[i]]
        else obj2[s[i]] = (obj2[s[i]] || 0) - 1
        i += 1

        if (_.isEqual(obj1, obj2)) output.push(i)

        j += 1
    }

    return output
};