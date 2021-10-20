import unittest
from main import CalcFigures

class TestCalc(unittest.TestCase):

    def setUp(self):
        self.calcfigures = CalcFigures()

    def test_square_quad(self):
        self.assertEqual(self.calcfigures.square_quad(4), 16)

    def test_square_quad(self):
        self.assertEqual(self.calcfigures.square_quad(-4), "Неверный ввод")

    def test_square_quad(self):
        self.assertEqual(self.calcfigures.square_quad(0), "Неверный ввод")

    def test_square_circle(self):
        self.assertEqual(self.calcfigures.square_circle(2), 12.566)

    def test_square_rectangle(self):
        self.assertEqual(self.calcfigures.square_rectangle(-2, 4), "Неверный ввод")

    def test_square_rectangle(self):
        self.assertEqual(self.calcfigures.square_rectangle(0, 4), "Неверный ввод")

    def test_square_rectangle(self):
        self.assertEqual(self.calcfigures.square_rectangle(2, -4), "Неверный ввод")

    def test_square_rectangle(self):
        self.assertEqual(self.calcfigures.square_rectangle(3, 0), "Неверный ввод")

    def test_square_triangle(self):
        self.assertEqual(self.calcfigures.square_triangle(-3, 8), "Неверный ввод")

    def test_square_triangle(self):
        self.assertEqual(self.calcfigures.square_triangle(3, -8), "Неверный ввод")

    def test_quare_parallelogram(self):
        self.assertEqual(self.calcfigures.square_parallelogram(5, 7), 35)

    def test_quare_parallelogram(self):
        self.assertEqual(self.calcfigures.square_parallelogram(-5, 7), "Неверный ввод")

    def test_quare_parallelogram(self):
        self.assertEqual(self.calcfigures.square_parallelogram(5, -7), "Неверный ввод")

if __name__ == 'main':
    unittest.main()
