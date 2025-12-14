class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        output = [0] * len(boxes)
        moves = 0
        balls = 0

        for i in range(len(boxes)):
            output[i] = moves + balls
            moves += balls
            if (boxes[i] == "1"):
                balls += 1

        moves = 0
        balls = 0
        print(output)
        for i in range(len(boxes) - 1, -1, -1):
            output[i] += moves + balls

            moves += balls
            if (boxes[i] == "1"):
                balls += 1

        return output
        