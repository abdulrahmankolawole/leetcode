class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        l = 0
        r = len(products) - 1
        products.sort()
        output = []

        for i in range(len(searchWord)):
            char = searchWord[i]

            while (l <= r and (len(products[l]) <= i or products[l][i] != char)):
                l += 1
            while (l <= r and (len(products[r]) <= i or products[r][i] != char)):
                r -= 1

            output.append([])
            distance = r - l + 1

            for i in range(min(distance, 3)):
                output[-1].append(products[l + i])

        return output
        