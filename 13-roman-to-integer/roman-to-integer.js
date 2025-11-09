var romanToInt = function(s) {
    let output = 0
    let lookup = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1,
    }

    for (let i = 0; i < s.length; i++) {
        if (lookup[s[i]] < lookup[s[i + 1]]) output -= lookup[s[i]]
        else output += lookup[s[i]]
    }

    return output
};