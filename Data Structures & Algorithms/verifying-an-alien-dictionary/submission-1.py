class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        for i,ch in enumerate(order):
            order_map[ch] = i
        
        for i in range(1,len(words)):
            w1,w2 = words[i-1], words[i]
            flag = True
            for j in range(min(len(w1),len(w2))):
                if order_map[w1[j]] > order_map[w2[j]]:
                    return False
                elif order_map[w1[j]] == order_map[w2[j]]:
                    continue
                else:
                    flag = False
                    break
            if flag:
                if len(w1) > len(w2):
                    return False
        return True