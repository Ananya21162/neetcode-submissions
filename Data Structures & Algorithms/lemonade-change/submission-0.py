class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill_count = {5:0,10:0,20:0}
        # bills = [5,10,5,5,20]
# bill_count = {5:2,10:1,20:0}
        for bill in bills:
            if bill == 5:
                bill_count[5] += 1
            elif bill == 10:
                if bill_count[5] < 1:
                    return False
                bill_count[5] -= 1
                bill_count[10] += 1
            else:
                if bill_count[10] > 0 and bill_count[5] > 0:
                    bill_count[10] -= 1
                    bill_count[5] -= 1
                elif bill_count[5] > 2 :
                    bill_count[5] -= 3
                else:
                    return False
        return True
                
                 
