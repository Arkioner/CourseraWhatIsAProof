class HanoiTowers:
    def __init__(self, disks):
        self.disks = disks
        self.moves = 0

    def run(self):
        #self.moves = pow(2, self.disks) - 1
        print(self.iterate(
            self.disks, origin_tower=list(reversed(range(1, self.disks + 1))), auxiliary_tower=[], destiny_tower=[])
        )
        return self.moves

    def iterate(self, n, origin_tower, auxiliary_tower, destiny_tower):
        if n == 1:
            destiny_tower.append(origin_tower.pop())
            self.moves += 1
            return destiny_tower
        auxiliary_tower = self.iterate(n - 1, origin_tower, destiny_tower, auxiliary_tower)
        destiny_tower.append(origin_tower.pop())
        self.moves += 1
        self.iterate(n - 1, auxiliary_tower, origin_tower, destiny_tower)
        return destiny_tower
