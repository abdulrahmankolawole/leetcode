var minOperations = function(boxes) {
    let output = new Array(boxes.length).fill(0)
    let moves = 0
    let balls = 0

    for (let i = 0; i < boxes.length; i++) {
        let ball = parseInt(boxes[i])
        output[i] = balls + moves
        moves += balls
        balls += ball
    }    

    balls = 0
    moves = 0
    for (let i = boxes.length - 1; i >= 0; i--) {
        let ball = parseInt(boxes[i])
        output[i] += balls + moves
        moves += balls
        balls += ball
    }

    return output
};