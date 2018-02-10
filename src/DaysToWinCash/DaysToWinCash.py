import math


class DaysToWinCash:
    # Compute the number of the first day when your wealth will exceed *target_amount*,
    # if you start with *starting_amount* of cash and earn *earn_percent* percents every day

    def DayToReachTarget(self, starting_amount, earn_percent, target_amount):
        day = 1
        amount = starting_amount
        day_multiplier = (1 + (earn_percent) / 100.0)
        while amount < target_amount:
            day += 1
            amount = amount * day_multiplier
        return day

    # Compute the number of the first day when your wealth will exceed *target_amount*,
    # if you start with *starting_amount* of cash and earn *earn_percent* percents every day
    def DayToReachTarget2(self, starting_amount, earn_percent, target_amount):
        days_to_reach_target = math.log(target_amount, (1 + earn_percent / 100.0))
        days_to_reach_starting = math.log(starting_amount, (1 + earn_percent / 100.0))
        return 1 + math.ceil(days_to_reach_target - days_to_reach_starting)

    def PrintFirstDay2(self, starting_amount, earn_percent, target_amount, days):
        print(
            "Cou: If you start with $%d and earn %d%% each day, you will have more than $%d on day %d for the first time!" %
            (starting_amount, earn_percent, target_amount, days))

    def run(self, starting_amount, earn_percent, target_amount):
        self.PrintFirstDay2(starting_amount, earn_percent, target_amount,
                            (self.DayToReachTarget(starting_amount, earn_percent, target_amount)))
        self.PrintFirstDay2(starting_amount, earn_percent, target_amount,
                            (self.DayToReachTarget2(starting_amount, earn_percent, target_amount)))

instance = DaysToWinCash()
# Prints when you will get more than $1000000 for the first time, if you start with $1000
# and earn 2% every day.
instance.run(1000, 10, 1000000)
