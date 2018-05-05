from unittest import TestCase

from src.Modular.TileARectangleWithSquares import squares


class TestSuite(TestCase):

    def test10x6(self):
        self.assertEqual(15, squares(10, 6))

    def test6x10(self):
        self.assertEqual(15, squares(6, 10))

    def test2x2(self):
        self.assertEqual(1, squares(2, 2))

    def test3x3(self):
        self.assertEqual(1, squares(3, 3))

    def test4x4(self):
        self.assertEqual(1, squares(4, 4))

    def test6x6(self):
        self.assertEqual(1, squares(6, 6))

    def test_squares(self):
        given_horizontal = 10
        given_vertical = 6
        expected_number_of_squares = 15
        self.assertEqual(expected_number_of_squares, squares(given_horizontal, given_vertical))

    def test_squares_given_equals_horizontal_and_vertical(self):
        given_horizontal = 10
        given_vertical = 10
        expected_number_of_squares = 1
        self.assertEqual(expected_number_of_squares, squares(given_horizontal, given_vertical))

    def test_squares_given_fucking_big_numbers(self):
        given_horizontal = 790933790547
        given_vertical = 1849639579327
        expected_number_of_squares = 125316338661
        self.assertEqual(expected_number_of_squares, squares(given_horizontal, given_vertical))
