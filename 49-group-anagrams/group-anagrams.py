class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = {}

        for word in strs:
            array = [char for char in word]
            array.sort()
            anagram = "".join(array)

            if (anagram not in lookup):
                lookup[anagram] = []
            lookup[anagram].append(word)

        output = [item for item in lookup.values()]
        return output     