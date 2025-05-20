class Solution:
    def frequencySort(self, s: str) -> str:
        lookup = Counter(s)
        buckets = defaultdict(list)
        n = len(s)
        result = ""

        for char, count in lookup.items():
            buckets[count].append(char)

        for i in range(n, 0 , -1):
            for char in buckets[i]:
                result += char * i


        return result
        