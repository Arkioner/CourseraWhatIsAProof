class HanoiTowers:
    def __init__(self, disks):
        self.disks = disks
        self.moves = 0

    def run(self):
        print(self.iterate(
            self.disks, list(reversed(range(1, self.disks + 1))), [], [])
        )
        return self.moves

    def move(self, origin_tower, destiny_tower):
        value = origin_tower.pop()
        destiny_tower.append(value)
        self.moves += 1

    def iterate(self, n, origin_tower, auxiliary_tower, destiny_tower):
        if n == 1:
            self.move(origin_tower, destiny_tower)
            return destiny_tower
        auxiliary_tower = self.iterate(n - 1, origin_tower, destiny_tower, auxiliary_tower)
        self.move(origin_tower, destiny_tower)
        return self.iterate(n - 1, auxiliary_tower, origin_tower, destiny_tower)

