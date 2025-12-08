class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = 0
        j = len(people) - 1
        boats = 0

        while (i <= j):
            diff = limit - people[j]

            if (diff >= people[i]):
                i += 1
            j -= 1
            boats += 1

        return boats