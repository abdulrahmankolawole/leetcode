var minOperations = function(boxes) {
    let output = new Array(boxes.length).fill(0)
    let moves = 0
    let balls = 0

    for (let i = 0; i < boxes.length; i++) {
        output[i] = balls + moves
        moves = moves + balls
        if (boxes[i] == "1") balls ++
    }
    balls = 0
    moves = 0
    for (let i = boxes.length - 1; i >= 0; i--) {
        output[i] += balls + moves
        moves = moves + balls
        if (boxes[i] == "1") balls ++
    }

    return output
};