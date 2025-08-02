class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        left = 0
        right = len(products) - 1
        output = []

        for i in range(len(searchWord)):
            char = searchWord[i]

            while (left <= right and (len(products[left]) <= i or products[left][i] != char)):
                left += 1
            
            while (left <= right and (len(products[right]) <= i or products[right][i] != char)):
                right -= 1

            distance = right - left + 1
            
            output.append([])
            for k in range(min(3, distance)):
                output[-1].append(products[k + left])

        return output
        