class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = []
        for i in range(len(position)):
            cars.append([position[i],speed[i]])
        cars.sort(key = lambda x: x[0],reverse= True)
        for car in cars:
            time = (target-car[0])/car[1]
            if stack:
                if stack[-1] >= time:
                    # no need to append the new time
                    continue
                else:
                    stack.append(time)
            else:
                stack.append(time)
        return len(stack)