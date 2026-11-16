class TimeMap:

    def __init__(self):
        self.keyMapValues = {}
        self.keyMapTime = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.keyMapValues:
            self.keyMapValues[key].append(value)
            self.keyMapTime[key].append(timestamp)
        else:
            self.keyMapValues[key] = [value]
            self.keyMapTime[key] = [timestamp]


    def get(self, key: str, timestamp: int) -> str:
        
        if key in self.keyMapValues:
            times = self.keyMapTime[key]
            l, r = 0 , len(times)-1
            ans = float('inf')
            while l <= r:
                mid = (l+r)//2
                if times[mid] <= timestamp:
                    ans = mid 
                    l = mid+1
                else:
                    r = mid - 1
            return "" if ans == float('inf') else self.keyMapValues[key][ans]
        else:
            return ""