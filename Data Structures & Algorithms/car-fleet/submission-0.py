class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        car = sorted(
            [(position[i], speed[i]) for i in range(len(position))], reverse=True
        )  # we can use zip here to create tuple of 2 lists as well
        fleet, ahead = 0, 0
        for pos, spd in car:
            time = (target - pos) / spd
            if time > ahead:
                fleet += 1
                ahead = time
        return fleet
