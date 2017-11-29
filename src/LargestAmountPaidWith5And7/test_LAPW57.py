from unittest import TestCase

from src.LargestAmountPaidWith5And7.LAPW57 import LAPW57


class TestLAPW57(TestCase):
    def test_change(self):
        instance = LAPW57()
        self.assertSequenceEqual(instance.change(25), [5, 5, 5, 5, 5])
