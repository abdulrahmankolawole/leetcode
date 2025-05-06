class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find candidate row
        # perform binary search on matrix

        def isCandidateRow(array, val):
            i = 0
            j = len(array) - 1
            return array[i] <= val <= array[j]

        def binary_search(array, val):
            i = 0
            j = len(array) - 1

            while (i <= j):
                mid = (i + j) // 2
                if (array[mid] == val):
                    return True
                if (val < array[mid]):
                    j = mid - 1
                else:
                    i = mid + 1

            return False
        
        i = 0
        j = len(matrix) - 1

        while (i <= j):
            mid = (i + j) // 2

            if (isCandidateRow(matrix[mid], target)):
                return binary_search(matrix[mid], target)
            if (target < matrix[mid][0]):
                j = mid - 1
            else:
                i = mid + 1

        
        return False

        