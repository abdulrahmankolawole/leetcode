var checkInclusion = function(s1, s2) {
    const _ = require('lodash');

    let lookup1 = {};
    let lookup2 = {};

    if (s1.length > s2.length) return false;

    for (let i = 0; i < s1.length; i++) {
        let curr = s1[i];
        if (!(curr in lookup1)) lookup1[curr] = 0;
        lookup1[curr] += 1;
    }   

    for (let i = 0; i < s1.length; i++) {
        let curr = s2[i];
        if (!(curr in lookup2)) lookup2[curr] = 0;
        lookup2[curr] += 1;
    }

    // Compare initial counts
    if (_.isEqual(lookup1, lookup2)) {
        return true;
    }

    let i = 0;
    let j = s1.length;

    while (j < s2.length) {
        let curr = s2[j];

        if (!(curr in lookup2)) lookup2[curr] = 0;
        lookup2[curr] += 1;

        // Remove the character that is sliding out of the window
        if (lookup2[s2[i]] === 1) {
            delete lookup2[s2[i]];
        } else {
            lookup2[s2[i]] -= 1;
        }

        i += 1;
        j += 1;

        // Compare counts after updating
        if (_.isEqual(lookup1, lookup2)) {
            return true;
        }
    }

    return false;
};