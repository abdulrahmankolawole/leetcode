class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        arr_one = sentence1.split(" ") 
        arr_two = sentence2.split(" ") 

        if (len(arr_two) < len(arr_one)):
            arr_one, arr_two = arr_two, arr_one

        i = 0
        a = 0
        while (i < len(arr_one) and a < len(arr_two)  and arr_one[i] == arr_two[i]):
            i += 1

        
        j = len(arr_one) - 1
        b = len(arr_two) - 1
        while (j >= 0 and b >= 0 and arr_one[j] == arr_two[b]):
            j -= 1
            b -= 1
            
        
        return i > j