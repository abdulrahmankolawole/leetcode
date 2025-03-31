var maxArea = function(height) {
    let i = 0
    let j = height.length - 1
    let output = 0

    while (i < j) {
        let area = Math.min(height[i], height[j]) * (j - i)
        output = Math.max(output, area)
        if (height[i] < height[j]) i += 1
        else j -= 1
    }   

    return output 
};