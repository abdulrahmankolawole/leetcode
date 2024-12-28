
var strStr = function(haystack, needle) {
    let result = haystack.split(needle)
    if (result.length > 1) return result[0].length
    return - 1    
};