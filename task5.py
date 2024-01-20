# На семинарах по ООП был создан класс прямоугольник хранящий длину и ширину,
# а также вычисляющую периметр, площадь и позволяющий складывать и вычитать прямоугольники беря за основу периметр.
# Напишите 3-7 тестов unittest для данного класса.
import unittest
from rectangle import Rectangle


class TestUnitRectangle(unittest.TestCase):

    def setUp(self) -> None:
        self.r1 = Rectangle(5, 8)
        self.r2 = Rectangle(3, 5)

    def test_1(self):
        with self.assertRaisesRegex(ValueError, "Сторона не может быть отрицательной"):
            self.r1.width = -5

    def test_2(self):
        with self.assertRaisesRegex(TypeError, "Не поддерживается сложение с этим типом"):
            self.r1 + 5

    def test_3(self):
        self.assertEqual(self.r1.perimeter(), 80)
        self.assertEqual(self.r2.perimeter(), 30)

    def test_4(self):
        self.assertEqual(self.r1.area(), 40)
        self.assertEqual(self.r2.area(), 15)

    def test_5(self):
        self.assertEqual(self.r1 + self.r2, Rectangle(3, 52))

    def test_6(self):
        self.assertGreater(self.r1, self.r2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
