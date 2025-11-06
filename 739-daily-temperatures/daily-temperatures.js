var dailyTemperatures = function(temperatures) {
    let output = new Array(temperatures.length).fill(0)
    let stack = []

    for (let i = temperatures.length - 1; i >= 0; i--) {
        let current = temperatures[i]
        if (!stack.length) {
            stack.push([current, i])        
        }
        else {
            while (stack.length && current >= stack.at(-1)[0]) {
                stack.pop()
            }
            if (stack.length) {
                output[i] = stack.at(-1)[1] - i
            }
            stack.push([current, i])
        }
    } 

    return output
};