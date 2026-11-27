class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # position の降順（ゴールに近い順）にソート
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        prev_time = 0.0  # 直前の独立した車群がゴールに着く時間

        for pos, spd in cars:
            time = (target - pos) / spd
            # 前の車群より到着が遅い（＝追いつけない）なら新しいフリート
            if time > prev_time:
                fleets += 1
                prev_time = time

        return fleets