class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        arr1 = sentence1.split(" ")
        arr2 = sentence2.split(" ")

        if (len(arr2) < len(arr1)):
            arr1, arr2 = arr2, arr1

        i = 0
        j = len(arr1) - 1
        k = len(arr2) - 1

        while (i < len(arr1) and arr1[i] == arr2[i]):
            i += 1

        while (j >= 0 and k >= 0 and arr1[j] == arr2[k]):
            j -= 1
            k -= 1

        return i > j
        