class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        l, r = 0, n-1
        boats = 0
        while l < r:
            weight = people[l] + people[r]
            boats += 1
            if weight <= limit:
                
                l += 1
                r -= 1
            else:
                r -= 1
        if l == r:
            boats += 1
        return boats