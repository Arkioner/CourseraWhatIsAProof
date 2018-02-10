from unittest import TestCase

from src.DaysToWinCash.DaysToWinCash import DaysToWinCash


class TestDaysToWinCash(TestCase):
    def test_run_n_checks(self):
        instance = DaysToWinCash()
        starting_amount = 100
        earn_percent = 2
        for target_amount in range(starting_amount, 4165465487, 45678):
            days_coursera = instance.DayToReachTarget(starting_amount, earn_percent, target_amount)
            days_us = instance.DayToReachTarget2(starting_amount, earn_percent, target_amount)
            self.assertEqual(days_coursera, days_us)
            instance.PrintFirstDay2(starting_amount, earn_percent, target_amount, days_us)

    def test_run_n_checks_coursera(self):
        instance = DaysToWinCash()
        starting_amount = 100
        earn_percent = 2
        for target_amount in range(starting_amount, 4165465487, 45678):
            days_coursera = instance.DayToReachTarget(starting_amount, earn_percent, target_amount)
            instance.PrintFirstDay2(starting_amount, earn_percent, target_amount, days_coursera)

    def test_run_n_checks_us(self):
        instance = DaysToWinCash()
        starting_amount = 100
        earn_percent = 2
        for target_amount in range(starting_amount, 4165465487, 45678):
            days_us = instance.DayToReachTarget2(starting_amount, earn_percent, target_amount)
            instance.PrintFirstDay2(starting_amount, earn_percent, target_amount, days_us)