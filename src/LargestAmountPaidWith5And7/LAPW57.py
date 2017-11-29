class LAPW57:

    def change(self, amount):
        if amount == 24:
            return [5, 5, 7, 7]
        if amount == 25:
            return [5, 5, 5, 5, 5]
        if amount == 26:
            return [5, 7, 7, 7]
        if amount == 27:
            return [5, 5, 5, 5, 7]
        if amount == 28:
            return [7, 7, 7, 7]

        coins = self.change(amount - 5)
        coins.append(5)
        return coins
