from unittest import TestCase

from src.DeliveryProblem.AverageWeight import average
from src.DeliveryProblem.Utils import DeliveryUtils


class TestDaysToWinCash(TestCase):

    def test_average_weight(self):
        graph = DeliveryUtils.get_graph([(178, 212), (287, 131), (98, 156)])
        self.assertEqual(424.1000397032701, average(graph))
