class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, spd in cars:
            time = (target - pos) / spd
            if stack and time <= stack[-1]:
                continue  # merges into the fleet ahead, push nothing
            stack.append(time)  # new fleet

        return len(stack)
