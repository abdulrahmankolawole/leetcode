var decodeString = function(s) {
    let stack = []

    for (let char of s) {
        if (char != "]") {
            stack.push(char)
        } 
        else {
            let str = ""
            while (stack.length && stack.at(-1) != "[") {
                str = stack.pop() + str
            }
            if (stack.length) {
                stack.pop()
            }
            k = ""
            while (stack.length && !isNaN(stack.at(-1))) {
                k = stack.pop() + k
            }
            stack.push(str.repeat(parseInt(k)))

        }
    }    
    return stack.join("")
};