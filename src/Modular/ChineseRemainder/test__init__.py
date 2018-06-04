from unittest import TestCase

from src.Modular.ChineseRemainder import ChineseRemainderTheorem


class TestSuite(TestCase):

    def test_ChineseRemainderTheorem(self):
        self.assertEqual(579510303168901, ChineseRemainderTheorem(686579304, 295310485, 26855093, 8217207))
