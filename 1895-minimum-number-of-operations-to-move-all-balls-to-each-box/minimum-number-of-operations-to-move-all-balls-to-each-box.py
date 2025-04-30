class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = [0 for _ in range(len(boxes))]
        moves = 0
        balls = 0

        for i in range(len(boxes)):
            result[i] = balls + moves
            moves += balls
            balls += int(boxes[i])
        
        balls = 0
        moves = 0
        for i in range(len(boxes) - 1, -1, -1):
            result[i] += balls + moves 
            moves += balls
            balls += int(boxes[i])

        
        return result


        
        