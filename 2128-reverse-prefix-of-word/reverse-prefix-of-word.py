class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        def reverseWord(string, i, j):
            
            arr = [char for char in string]

            while (i < j):
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

            return "".join(arr)

        try:
            index = word.index(ch)
        
        except ValueError:
            return word

        if (not index):
            return word
        
        return reverseWord(word, i = 0, j = index)
        