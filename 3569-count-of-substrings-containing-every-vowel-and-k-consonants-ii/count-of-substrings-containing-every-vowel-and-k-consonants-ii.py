class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:

        def atLeastK(k):
            lookup = defaultdict(int)
            consonants = 0
            output = 0
            j = 0
            i = 0
            vowels = set("aeiou")

            while (j < len(word)):
                if (word[j] in vowels):
                    lookup[word[j]] += 1
                else:
                    consonants += 1

                while (len(lookup) == 5 and consonants >= k):
                    output += len(word) - j

                    if (word[i] in vowels):
                        lookup[word[i]] -= 1
                    else:
                        consonants -= 1
                    if (lookup[word[i]] == 0):
                        lookup.pop(word[i])
                    i += 1

                j += 1

            return output

        return atLeastK(k) - atLeastK(k + 1)

        