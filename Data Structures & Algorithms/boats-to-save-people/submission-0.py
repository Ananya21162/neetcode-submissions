class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people)-1
        maxBoat = 0
        while (l<r):
            if (people[l]+people[r]<=limit):
                l += 1
                r -= 1
                maxBoat += 1
            else:
                maxBoat += 1
                r -= 1
        if l == r:
            maxBoat += 1
        return maxBoat