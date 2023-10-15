from unittest import TestCase
from scratch.main import add, subt


class Test(TestCase):
    def test_add_two_integers(self):
        self.assertEqual(add(1, 2), 3, msg="Test case failed!")

    def test_add_string_and_number(self):
        self.assertRaises(TypeError, add, a='1.2', b=2)

    def test_subt_two_numbers(self):
        self.assertEqual(subt(10, 2), 8)
