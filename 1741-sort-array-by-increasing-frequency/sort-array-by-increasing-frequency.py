class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        output = []
        counter = Counter(nums)
        buckets = {}
        n = len(nums)

        for num, freq in counter.items():
            if (freq not in buckets):
                buckets[freq] = []
            buckets[freq].append(num)

        print(buckets)
                
        for freq in range(1, n + 1):
            if (freq in buckets):
                numbers = buckets[freq]

                numbers.sort(reverse=True)

                print("numbers: ", numbers)

                for num in numbers:
                    for _ in range(freq):
                        output.append(num)

        return output   