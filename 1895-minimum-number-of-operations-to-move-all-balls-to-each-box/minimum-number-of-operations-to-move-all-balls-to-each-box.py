class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = [None] *len(boxes)

        for i in range(len(boxes)):
            ball = boxes[i]

            operations = 0
            total_moves = 0
            for j in range(len(boxes)):
                if (boxes[j] != "0"):
                    moves = abs(j - i)
                    total_moves += moves
            
            result[i] = total_moves
        return result


        
    

        