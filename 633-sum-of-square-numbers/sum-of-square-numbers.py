class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = math.ceil(math.sqrt(c))


        while (i <= j):
            sum = (i ** 2) + (j ** 2)
            if (sum == c):
                return True
            elif (sum < c):
                i += 1
            else:
                j -= 1
        
        return False
        