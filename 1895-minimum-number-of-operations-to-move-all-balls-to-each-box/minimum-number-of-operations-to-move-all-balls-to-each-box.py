class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = [None] *len(boxes)

        for i in range(len(boxes)):
            ball = boxes[i]

            operations = 0
            total_moves = 0
            for j in range(i + 1, len(boxes)):
                if (boxes[j] != "0"):
                    # moves = abs(j - i)
                    # total_moves += moves
                    total_moves += abs(j - i)

            for j in range(i -1, -1, -1):
                if (boxes[j] != "0"):
                    total_moves += abs(j - i)
            
            result[i] = total_moves
        return result


        
    

        