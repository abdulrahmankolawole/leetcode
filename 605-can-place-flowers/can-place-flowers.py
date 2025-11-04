class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if (n == 0):
            return True
        
        for idx, val in enumerate(flowerbed):

            if (val == 0):
                left_is_empty = idx == 0 or flowerbed[idx - 1] == 0
                right_is_empty = idx == len(flowerbed) - 1 or flowerbed[idx + 1] == 0

                if (left_is_empty and right_is_empty):
                    n -= 1
                    flowerbed[idx] = 1

                if (n == 0):
                    return True

        
        return False
