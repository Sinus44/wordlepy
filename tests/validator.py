import unittest

import wordvalidator


class ValidatorTestCase(unittest.TestCase):
    def setUp(self):
        self.validator = wordvalidator.RuWordValidator

    def test_register(self):
        self.assertEqual(self.validator.validate("кот"), True)
        self.assertEqual(self.validator.validate("Кот"), True)
        self.assertEqual(self.validator.validate("КОТ"), True)
        self.assertEqual(self.validator.validate("Коты"), False)

    def test_all_right(self):
        self.assertEqual(self.validator.validate("Золото"), True)

    def test_invalid_word(self):
        self.assertEqual(self.validator.validate("бмга"), False)


if __name__ == '__main__':
    unittest.main()
