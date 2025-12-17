class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:

        def atLeastK(k):
            vowels = defaultdict(int)
            consonants = 0
            output = 0
            j = 0
            i = 0
            lookup = set("aeiou")

            while (j < len(word)):
                if (word[j] in lookup):
                    vowels[word[j]] += 1
                else:
                    consonants += 1

                while (len(vowels) == 5 and consonants >= k):
                    output += len(word) - j

                    if (word[i] in lookup):
                        vowels[word[i]] -= 1
                    else:
                        consonants -= 1
                    if (vowels[word[i]] == 0):
                        vowels.pop(word[i])
                    i += 1

                j += 1

            return output

        return atLeastK(k) - atLeastK(k + 1)

        