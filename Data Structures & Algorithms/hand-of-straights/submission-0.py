class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq_map = {}
        groups = len(hand)/groupSize
        if int(groups) != groups:
            return False
        hand.sort()
        for val in hand:
            freq_map[val] = freq_map.get(val,0)+1
        
        for i in range(int(groups)):
            keys = list(freq_map.keys())
            # print(keys)
            start = keys[0]
            for j in range(groupSize):
                if start not in freq_map:
                    return False
                freq_map[start] -= 1
                if freq_map[start] <= 0:
                    del freq_map[start]
                start += 1
        return True
            
                