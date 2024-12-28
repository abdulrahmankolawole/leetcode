var checkInclusion = function(s1, s2) {
    const _ = require('lodash');
    if (s1.length > s2.length) return false;

    let obj1 = {};
    let obj2 = {};

    // Populate obj1
    for (let i = 0; i < s1.length; i++) {
        obj1[s1[i]] = (obj1[s1[i]] || 0) + 1;
        obj2[s2[i]] = (obj2[s2[i]] || 0) + 1;
    }

    // Compare initial counts
    if (_.isEqual(obj1, obj2)) {
        return true;
    }

    let i = 0;
    for (let j = s1.length; j < s2.length; j++) {
        // Add the next character in s2
        obj2[s2[j]] = (obj2[s2[j]] || 0) + 1;

        // Remove the oldest character from s2
        if (obj2[s2[i]] === 1) {
            delete obj2[s2[i]];
        }
        else obj2[s2[i]] -= 1;

        i += 1;

        if (_.isEqual(obj1, obj2)) {
        return true;
        }
    }

    return false;
};