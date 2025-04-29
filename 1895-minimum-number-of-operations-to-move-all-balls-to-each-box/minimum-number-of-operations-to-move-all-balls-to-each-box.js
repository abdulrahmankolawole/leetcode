var minOperations = function(boxes) {
    let result = new Array(boxes.length).fill(0)
    let moves = 0
    let balls = 0
    for (let i = 0; i < boxes.length; i++) {
        result[i] = balls + moves
        moves = moves + balls
        balls +=  parseInt(boxes[i])
    }  

    moves = 0
    balls = 0
    for (let i = boxes.length - 1; i >= 0; i--) {
        result[i] += balls + moves
        moves = moves + balls
        balls +=  parseInt(boxes[i])
    }   
    return result

};